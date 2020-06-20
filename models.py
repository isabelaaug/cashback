from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///cashback.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    public_id = Column(Integer)
    nome_completo = Column(String(60))
    cpf = Column(Integer, index=True, unique=True)
    email = Column(String(40), index=True, unique=True)
    senha = Column(String(20))
    token = Column(String)

    def __repr__(self):
        return f'<Usuario {self.id}>'

    def save(self):
        db_session.add(self)
        db_session.commit()


class Compras(Base):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True)
    data = Column(String(10))
    valor = Column(Integer)
    cpf_compra = Column(Integer, ForeignKey('usuarios.cpf'))
    usuario = relationship('Usuarios')
    status = Column(String(40))
    percent_cashback = Column(Integer)
    cashback = Column(Integer)

    def __repr__(self):
        return f'<Compra {self.codigo}>'

    def save(self):
        db_session.add(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
