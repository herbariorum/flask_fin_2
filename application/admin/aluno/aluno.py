from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from application.auth.auth import login_required
from ..aluno.models import Aluno
from application import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

aluno = Blueprint("aluno", __name__, template_folder='templates',static_folder='static')


@aluno.route('/index', methods=['GET'], defaults={"pages": 1})
@aluno.route('/<int:pages>', methods=['GET'])
@login_required
def index(pages):
    per_page = 12
    error_out = False
    try:
        aluno = Aluno.query.order_by(Aluno.nome.desc()).paginate(pages, per_page)
    except SQLAlchemyError:
        flash("No users in the database", "error")
        rows = None
    return render_template('index.html', rows = aluno,error_out=False)


@aluno.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    aluno = Aluno.query.filter_by(id=id).first()
    if request.method == 'POST':
        try:
            id = id
            aluno.nome = request.form['nome']
            aluno.cpf = request.form['cpf']
            data_str = request.form['nascimento']
            data_str = data_str.split("/")
            aluno.nascimento = datetime(int(data_str[2]), int(data_str[1]), int(data_str[0]))            
            
            db.session.commit()
            flash("Registro atualizado com sucesso", "success")
            return redirect(url_for('aluno.index'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash("Não foi possível atualizar o registro {}".format(e), "error")
            
                

    return render_template('edit.html', row=aluno)

@aluno.route('<int:id>/delete', methods=['GET','POST'])
def delete(id):    
    aluno = Aluno.query.filter_by(id=id).first()
    if request.method == 'POST':
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
            flash("Registro removido com sucesso", "success")
            return redirect(url_for('aluno.index'))
        abort(404)
    return render_template('delete.html', id=aluno.id)

