import os, sys
from flask import Flask
sys.path.append(os.getcwd())
from application import db
# acrescento os models para gerar as tabelas
from application.admin.aluno import models
from application.auth import models

app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../finance.db'
db.init_app(app)

if __name__=='__main__':
    with app.app_context():
        db.create_all()