import functools
import re
from werkzeug.security import generate_password_hash
from flask import (
    Blueprint, redirect, request, session, flash, url_for, render_template, g
)
from sqlalchemy.exc import SQLAlchemyError
from ..auth.models import User
from application import db


auth = Blueprint("auth", __name__, template_folder='templates',static_folder='static')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not 'email' in session.keys():
            return redirect("/auth/login")
        return view(**kwargs)
    return wrapped_view

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = (
            User.query.filter_by(id=user_id).first()
        )

@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        error = None
        tipo = None
        if not username or not check_string_len(username): 
            tipo = 'warning'         
            error = 'O nome do usuário é necessário e deve conter no mínimo 6 characteres'        
        elif not email or not valida_email(email):
            tipo = 'warning'
            error = 'Digite um email válido'
        elif not password or not check_string_len(password):
            tipo = 'warning'
            error = 'A senha de usuário é necessária e deve conter nom mínimo 6 digitos'
        if error is None:
            try:               
                password_hash = gera_hash(password)
                user = User(
                    username = username,
                    email = email,
                    password_hash = password_hash
                )                
                db.session.add(user)
                db.session.commit()
                flash('Usuário registrado', 'success')
            except SQLAlchemyError as e:
                db.session.rollback()
                tipo = 'warning'
                error = "O nome de usuário ou email já está cadastrado no banco de dados."                
            else:
                return redirect(url_for("auth.login"))
        flash(error, tipo)
    return render_template('register.html')

@auth.route('/login', methods=['GET','POST'])
def login():
    mensagem = None
    tipo = None
    if request.method == 'POST':        
        email = request.form['email']
        password = request.form['password'] 
        user = User.query.filter_by(email=email).first()

        if user is None:
            tipo = 'warning'
            mensagem = "Email incorreto"
        elif not user.verify_password(password):
            tipo = 'warning'
            mensagem = "Senha incorreta"
        if mensagem is None:
            session.clear()
            session['user_id'] = user.id 
            session['username'] = user.username
            session['email'] = user.email
            return redirect(url_for('admin.painel')) 
        flash(mensagem, tipo)
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('auth.login'))



def valida_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex, email)):
        return True
    else:
        return False

def check_string_len(string):
    if len(string) < 6:
        return False
    else:
        return True

def gera_hash(password):
    return generate_password_hash(password)