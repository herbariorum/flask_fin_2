from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)
    
    from application.auth.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    
    from application.admin.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')
    
    from application.admin.aluno.aluno import aluno
    app.register_blueprint(aluno, url_prefix='/admin/aluno')

    @app.route('/')
    def index():
        return 'Página principal'

    return app


