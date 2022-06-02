import wtforms

from .models import Aluno

class AlunoForm(wtforms.Form):
    nome = wtforms.StringField('Nome')
    cpf = wtforms.SearchField('CPF')
    nascimento = wtforms.DateField('Data Nascimento')
    sexo = wtforms.SelectField(
        'Sexo',
        choices=(
            (0, 'Masculino'),
            (1, 'Feminino')
        ), coerce=int
    )