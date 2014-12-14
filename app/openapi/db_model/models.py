from app import db
from passlib.apps import custom_app_context as password_context

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

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(64))
    servive_id= db.Column(db.Integer,ForeignKey('servive.servive_id'))

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

class HardWare(db.Model):
    __tablename__="hardware"
    id=db.Column(db.Integer,primary_key=True)
    server_name=db.Column(db.String(19))

    server_type=db.Column(db.String(28))
    
    #cpuinfo eg intel#2.4Ghz#2#2;inter#2.4Gz#1#4
    phycpu_count=db.Column(db.Intege)

    #mem basic info,unit:G
    #eg 2G#10;4G#20
    mem_size=db.Column(db.Intege)

    #disk basic info unit:G
    #like ssd#100#10;sas@500#8 means ssb 100G 10 and sas 500G 8 
    disk_info=db.Column(db.String(50))
    
    #there are more infos,but i only  write the above as a example
    def __init__(self,servive_name,server_type,phycpu_count,mem_size,disk_info):
        self.servive_name=servive_name
        self.server_type=server_type
        self.phycpu_count=phycpu_count
        self.mem_size=mem_size
        self.disk_info=disk_info
    def __repr__(self):
        return "server hardware info %r,%r" %(self.servive_name,server_type)

class IDC(db.Model):
    __tablename__="idc"
    id=db.Column(db.Intege,primary_key=True)
    idc_city=db.Column(db.String(10))
    idc_name=db.Column(db.String(10))
    idc_carrier=db.Column(db.String(10))
    def __init__(self,idc_city,idc_name,idc_carrier):
        self.idc_city=idc_city
        self.idc_name=idc_name
        self.idc_carrier=idc_carrier
    def __repr__(self):
        return  "idc info %r,%r,%r" %(self.idc_city,self.idc_name,self.idc_carrier)

class Server(db.Model):
    __tablename__="server"
    id=db.Column(db.Integer,primary_key=True)
    hostname=db.Column(db.String(10))
    #eg eth0#10.210.71.145;eth1#10.210.71.144
    ip_addr=db.Column(db.String(32))

    idc_id=db.Column(db.Integer,ForeignKey('idc.idc_id'))
    hardware_id=db.Column(db.Integer,ForeignKey('hardware.hardware_id'))
    servive_id=db.Column(db.Integer,ForeignKey('servive.servive_id'))
    user_id=db.Column(db.Integer,ForeignKey('users.user_id'))
    
    #os_info eg: linux2.6.6 win8.0.0 or others
    os_info=db.Column(db.String(50))

    def __init__(self,hostname,ip_addr,idc_id,hardware_id,servive_id,user_id,os_info):
        self.hostname=hostname
        self.ip_addr=ip_addr
        self.idc_id=idc_id
        self.hardware_id=hardware_id
        self.servive_id=servive_id
        self.user_id=user_id
        self.os_info=os_info

    def __repr__(self):
        return  "servive info: hostname:%r" % self.hostname

