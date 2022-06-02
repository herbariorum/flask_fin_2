from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from application.auth.auth import login_required
from datetime import datetime
from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from pycpfcnpj import cpf
from ..aluno.formulario import AlunoForm
from ..aluno.models import Aluno
from application import db

from ...filter.uteis import Uteis

aluno = Blueprint("aluno", __name__, template_folder='templates',static_folder='static')


# @aluno.route('/index', methods=['GET'], defaults={"pages": 1})
# @aluno.route('/<int:pages>', methods=['GET'])
# @login_required
# def index(pages):
#     per_page = 10
#     error_out = False
#     dados = Aluno.query.order_by(Aluno.nome.desc()).paginate(pages, per_page)
#     try:
#         aluno = Aluno.query.order_by(Aluno.nome.desc()).paginate(pages, per_page)
#     except SQLAlchemyError:
#         flash("No users in the database", "error")
#         rows = None
        
#     return render_template('index.html', rows = aluno,error_out=False)

# https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
@aluno.route('/index', methods=['GET'])
@login_required
def index():
    dados = Aluno.query
    return render_template('index.html', title='Paneil::Aluno', rows= dados)

@aluno.route('/new', methods=['GET','POST'])
def new():
    form = AlunoForm()

    return render_template('new.html', title='Aluno::New', form=form)


# sem o uso do wtforms
# @aluno.route('/new', methods=['GET','POST'])
# def new():
#     if request.method == 'POST':    
#         nome = request.form['nome']
#         ccpf = request.form['cpf']
#         checkCpfValido = cpf.validate(ccpf)
#         data_str = request.form['nascimento']
#         msg = None
#         tipo = None
#         if len(nome) <= 6:
#             msg = "O *nome não pode ter menos que seis caracteres"
#             tipo = 'warning'
#         elif len(ccpf) < 11:
#             msg = "O *cpf está em branco"
#             tipo = 'warning'
#         elif not checkCpfValido:
#             msg = "Entre com um CPF válido"
#             tipo = 'warning'   
#         elif len(data_str) < 8:
#             msg = "O *data nascimento está em branco"
#             tipo = 'warning'            
#         if msg is None:
#             try:
#                 y, m, d = data_str.split('-')
#                 nascimento = datetime(int(y), int(m), int(d))
#                 aluno = Aluno(
#                     nome = nome,
#                     cpf = Uteis.is_only_number(ccpf),
#                     sexo = "MASCULINO",
#                     nascimento = nascimento,
#                     created_on = date.today()
#                 )  
#                 db.session.add(aluno)
#                 db.session.commit()
#                 msg = "O registro foi cadastrado com sucesso"
#                 tipo = 'success'
#             except SQLAlchemyError as e:
#                 db.session.rollback()
#                 msg = "Não foi possível incluir o registro.\n O seguinte erro ocorreu: {}".format(e)
#                 tipo = 'error'
#             else:
#                 flash(msg, tipo)
#                 return redirect(url_for('aluno.index'))        
#         flash(msg, tipo)
#     return render_template('new.html')

# falta validar o cpf
@aluno.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    aluno = Aluno.query.filter_by(id=id).first()
    if request.method == 'POST':
        try:
            id = id
            aluno.nome = request.form['nome']
            aluno.cpf = Uteis.is_only_number(request.form['cpf'])
            data_str = request.form['nascimento']   
            y, m, d = data_str.split('-')
            nascimento = datetime(int(y), int(m), int(d))
            aluno.nascimento = nascimento
            aluno.updated_on = date.today()
            
            db.session.commit()
            flash("Registro atualizado com sucesso", "success")
            return redirect(url_for('aluno.index'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash("Não foi possível atualizar o registro {}".format(e), "error")

    return render_template('edit.html', row=aluno)

@aluno.route('<int:id>/view', methods=['GET'])
def view(id):   
    aluno = Aluno.query.filter_by(id=id).first() 
    return render_template('view.html', row=aluno)

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