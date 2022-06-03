import wtforms
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from .baseform import BaseForm
from .models import Aluno
from config import SECRET_KEY

class AlunoForm(FlaskForm):

    nome = wtforms.StringField('Nome', validators=[DataRequired(message="O campo é requerido"), Length(min=6, message="O campo deve ter no mínimo 6 caracteres")])
    cpf = wtforms.SearchField('CPF', validators=[DataRequired(message="O campo é requerido"), Length(min=11, max=18, message="O campo deve ter no mínimo 11 caracteres")])
    nascimento = wtforms.DateField('Data Nascimento', validators=[DataRequired(message="O campo é requerido")])
    sexo = wtforms.SelectField(
        'Sexo',
        choices=(
            (0, 'Masculino'),
            (1, 'Feminino')
        ), coerce=int
    )
    submit = wtforms.SubmitField('Submit')