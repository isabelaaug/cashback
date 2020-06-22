from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import Usuarios, Compras
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import uuid
import jwt
import datetime


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'


def token_required(req):
    @wraps(req)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'token ausente'}), 401
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = Usuarios.query.filter_by(public_id=data['public_id']).first()
        if current_user:
            return req(*args, **kwargs)
        else:
            return jsonify({'message': 'token inválido'}), 401
    return decorated


class Usuario(Resource):
    # POST - CADASTRAR USUÁRIOS
    def post(self):
        dados = request.json
        try:
            hashed_password = generate_password_hash(dados['senha'], method='sha256')
            usuario = Usuarios(
                nome_completo=dados['nome_completo'],
                cpf=dados['cpf'],
                email=dados['email'],
                senha=hashed_password,
                public_id=str(uuid.uuid4())
            )
            usuario.save()
            mensagem = f'Usuário {usuario.nome_completo} cadastrado com sucesso.'
            response = {
                'status': 'Sucesso',
                'message': mensagem
            }
        except:
            response = {
                'status': 'Error',
                'message': 'Este CPF e/ou e-mail já possui conta cadastrada.'
            }
        return response


class LoginUsuario(Resource):
    # POST - LOGIN DE USUARIO
    def post(self):
        auth = request.authorization
        user = Usuarios.query.filter_by(email=auth.username).first()

        if user and check_password_hash(user.senha, auth.password):
            token = jwt.encode({
                'public_id': user.public_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)},
                app.config['SECRET_KEY']
            )
            response = jsonify({
                'status': 'Sucesso',
                'message': 'Login realizado com sucesso.',
                'token': token.decode('UTF-8')})
            user.token = token.decode('UTF-8')
            user.save()
            return response
        else:
            response = {
                'status': 'Error',
                'message': 'E-mail ou senha inválida.'
            }
            return jsonify(response)


class Compra(Resource):
    # POST - CADASTRAR COMPRAS
    def post(self):
        dados = request.json
        if dados['cpf_compra'] == 15350946056:
            status = 'Aprovado'
        else:
            status = 'Em validação'
        if dados['valor'] > 1500:
            percent_cashback = 20
            cashback = dados['valor'] * 0.2
        elif dados['valor'] > 1000:
            percent_cashback = 15
            cashback = dados['valor'] * 0.15
        else:
            percent_cashback = 10
            cashback = dados['valor'] * 0.1
        try:
            compra = Compras(
                codigo=dados['codigo'],
                valor=dados['valor'],
                cpf_compra=dados['cpf_compra'],
                data=dados['data'],
                status=status,
                percent_cashback=percent_cashback,
                cashback=cashback
            )
            compra.save()
            response = {
                'status': 'Sucesso',
                'message': 'Compra cadastrada com sucesso.'
            }
        except:
            response = {
                'status': 'Error',
                'message': 'Código de compra já cadastrado.'
            }
        return response


class ListaCompras(Resource):
    # GET - LISTAR COMPRAS CADASTRADAS
    # @token_required
    def get(self, cpf):
        compras = Compras.query.filter_by(cpf_compra=cpf).all()
        if compras:
            response = [{
                'codigo': dados.codigo,
                'valor': dados.valor,
                'data': dados.data,
                'percent_cashback': dados.percent_cashback,
                'cashback': dados.cashback,
                'status': dados.status} for dados in compras]
        else:
            response = {
                'status': 'Error',
                'message': 'CPF não possui compras cadastradas.'
            }
        return response


class Cashback(Resource):
    # GET - LISTAR CASHBACK ACUMULADO (API)
    # @token_required
    def get(self, cpf):
        parametro = {'cpf': cpf}
        data = requests.get(
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback",
            params=parametro
        )
        resp = data.json()
        response = resp["body"]
        return response


# POST - CADASTRAR USUARIOS
api.add_resource(Usuario, '/cadastro/')
# POST - LOGIN USUARIO
api.add_resource(LoginUsuario, '/login/')
# POST - CADASTRAR COMPRAS
api.add_resource(Compra, '/cadastroCompra/')
# GET - LISTAR COMPRAS
api.add_resource(ListaCompras, '/compras/<int:cpf>/')
# GET - LISTAR CASHBACK ACUMULADO (API)
api.add_resource(Cashback, '/cashback/<int:cpf>/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
