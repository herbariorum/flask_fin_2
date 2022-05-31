from application import db

class Aluno(db.Model):
    __tablename__ = 'alunos_table'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11))
    nascimento = db.Column(db.Date, nullable=False)
    # created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
