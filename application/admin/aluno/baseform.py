from flask import request, session
from wtforms import Form
from wtforms.csrf.session import SessionCSRF
from config import SECRET_KEY
from datetime import timedelta

class BaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = SECRET_KEY
        csrf_time_limit = timedelta(minutes=20)

        