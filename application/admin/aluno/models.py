from application import db
import datetime


class Aluno(db.Model):
    __tablename__ = 'alunos_table'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11))
    nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(10))
    status = db.Column(db.SmallInteger(), default=1)
    created_on = db.Column(db.Date, default=datetime.date.today())
    updated_on = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'nascimento': self.nascimento,
            
        }
