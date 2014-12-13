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

class HardWare(db.Model):
    __tablename__="hardware"
    id=db.Column(db.Integer,primary_key=True)

    server_type=db.Column(db.String(28))
    
    #cpuinfo eg intel#2.4Ghz#2#2;inter#2.4Gz#1#4
    phycpu_count=db.Column(db.Intege)
    logicalcpu_count=db.Column(db.Intege)
    cpu_info=db.Column(db.String(28))

    #mem basic info,unit:G
    #eg 2G#10;4G#20
    mem_size=db.Column(db.Intege)
    mem_info=db.Column(db.String(28))

    #disk basic info unit:G
    #like ssd#100#10;sas@500#8 means ssb 100G 10 and sas 500G 8 
    disk_info=db.Column(db.String(50))

    #Network Interface Card NIC
    nic=db.Column(db.String(50))
class IDC(db.Model):
    __tablename__="inc"
    id=db.Column(db.Intege,primary_key=True)
    idc_name=db.Column(db.String(10))
    idc_carrier=db.Column(db.String(10))
class Server(db.Model):
    __tablename__="server"
    #os_info eg: linux2.6.6 win8.0.0 or others
    os_info=db.Column(db.String(50))
    
