from app import db
from passlib.apps import custom_app_context as password_context

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def set_password(self, password):
        self.password=self.hash_password(password)

    def set_username(self, username):
        self.username=username
class Servive(db.Model):
    __tablename__ = "servive"
    servive_id=db.Column(db.Integer,primary_key)
    servive_name=db.Column(db.String(20))
    servive_parent=db.Column(db.Integer)

    def __init__(self,servive_name,servive_parent):
        self.servive_name=servive_name
        self.servive_parent=servive_parent
    def __repr__(self):
        return "<servive info %r,%r,%r>" % (self.servive_id,self.servive_name,self.servive_parent)

