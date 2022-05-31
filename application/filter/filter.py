from dateutil.parser import *
from datetime import datetime

def datefilter(data, fmt=None):
    if isinstance(data, str):
        data = parse(data)
    else:        
        data = data
    
    native = data.replace(datetime.tzinfo==None)
    format = '%d/%m/%Y'
    return native.strftime(format)



