<h1 align="center">
<img src="https://github.com/isabelaaug/cashback/blob/master/assets/Grupo-boticario-logo.jpg" alt="logo">
<br>
<br>
CASHBACK - O BOTICÁRIO
</h1>
<p align="center">Desafio Dev Back-end – “Eu revendedor ‘O Boticário’ quero ter benefícios de acordo com o meu volume de vendas”.</p>

> Status do Projeto: Concluído. :heavy_check_mark: 

## Descrição do projeto :page_facing_up:

<p>Cashback quer dizer “dinheiro de volta”, e o sistema funciona de forma simples: o revendedor 
faz uma compra, cadastra e seu benefício vem com a devolução de parte do dinheiro gasto no mês seguinte.<br>
A API desenvolvida permite cadastra usuários e compras. Criando um banco de dados SQLite para registrar os dados, permite acompanhar 
as compras cadastradas e o retorno de cashback.</p>

## Funcionalidades :gear:

- Cadastro de usuário
- Login de usuário
- Cadastro de compras
- Visualização de compras cadastradas (filtrando pelo CPF)
- Visualização do total de cashback acumulado (filtrando pelo CPF)

## Linguagens, dependencias e libs utilizadas :books:

- Python
- Flask
- Flask-JWT
- Flask-RESTful
- SQLAlchemy
- SQLite
- Werkzeug
- Unittest

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 
```
git clone https://github.com/isabelaaug/cashback.git
```
Abra o projeto em um ambiente de desenvolvimento Python (PyCharm) e instale as dependêcias do projeto, executando no terminal:
```
pip install -r requirements.txt
```
Crie o bando de dados, executando o arquivo:
```
models.py
```
Para utilizar a aplicação, execute o arquivo:
```
app.py
```
<p>Para testar as rotas e métodos acessar http://127.0.0.1:8000/ utilizando programas como, o Postman ou Insomnia.
<br>
E para utilizar token, é necessário criar um usuário, realizar login, copiar o token gerado e inserir na Headers da requisição:
<br></p>
<p>
Tela de Login:
<br>
  <img src="https://github.com/isabelaaug/cashback/blob/master/assets/token%201.PNG" alt="token1">
<br></p>
<p>
Tela da requisição:
<br>
  <img src="https://github.com/isabelaaug/cashback/blob/master/assets/token%202.PNG" alt="token2">
<br></p>

## Desenvolvedores/Contribuintes :octocat:
Desenvolvido por Isabela Augusta de Oliveira. [Meu contato](https://www.linkedin.com/in/isabela-augusta-de-oliveira-8a50a8194/) :blush:
