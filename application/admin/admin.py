from flask import Blueprint, session, render_template, redirect
from application.auth.auth import login_required

admin = Blueprint("admin", __name__, template_folder='templates',static_folder='static')

# https://github.com/pallets/flask/blob/main/examples/tutorial/flaskr/auth.py

@admin.route("/painel")
@login_required
def painel():  
    return render_template('painel.html')

@admin.route("/aluno")
@login_required
def aluno():
    return render_template('admin/aluno/index.html')
    
@admin.route("/profile")
@login_required
def profile():
    id = session['user_id']
    return render_template('profile.html', user_id = id)