import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from application import db

class User(db.Model):
    __tablename__ = 'users_table'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)