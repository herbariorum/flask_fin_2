from dateutil.parser import *
from datetime import datetime
from .uteis import Uteis


def cpffilter(data):
    cpf = '{}.{}.{}-{}'.format(data[:3], data[3:6], data[6:9], data[9:])
    return cpf


def format_strit_to_data(data):
    ret = data.strftime('%d/%m/%Y')
    return ret

