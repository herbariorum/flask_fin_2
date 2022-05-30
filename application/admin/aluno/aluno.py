from flask import Blueprint, session, render_template
from application.auth.auth import login_required

aluno = Blueprint("aluno", __name__, template_folder='templates',static_folder='static')


@aluno.route('/index')
@login_required
def index():
    return render_template('index.html')