from app import db
from passlib.apps import custom_app_context as password_context

class Service(db.Model):
    __tablename__ = "service"
    service_id=db.Column(db.Integer,primary_key=True,index=True)
    service_name=db.Column(db.String(20))
    service_parent=db.Column(db.Integer)

    def __init__(self,service_name,service_parent):
        self.service_name=service_name
        self.service_parent=service_parent
    def __repr__(self):
        return "<service info %r,%r,%r>" % (self.service_id,self.service_name,self.service_parent)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True,unique=True)
    password = db.Column(db.String(64))
    service_id= db.Column(db.Integer,db.ForeignKey('service.service_id'))

    def __init__(self, username, password,service_id):
        self.username = username
        self.service_id=service_id
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def set_password(self, password):
        self.password=self.hash_password(password)

    def set_username(self, username):
        self.username=username

    def set_service_id(self,service_id):
        self.service_id=service_id

class HardWare(db.Model):
    __tablename__="hardware"
    hardware_id=db.Column(db.Integer,primary_key=True)
    server_name=db.Column(db.String(19))

    server_type=db.Column(db.String(28))
    
    #cpuinfo eg intel#2.4Ghz#2#2;inter#2.4Gz#1#4
    phycpu_count=db.Column(db.Integer)

    #mem basic info,unit:G
    #eg 2G#10;4G#20
    mem_size=db.Column(db.Integer)

    #disk basic info unit:G
    #like ssd#100#10;sas@500#8 means ssb 100G 10 and sas 500G 8 
    disk_info=db.Column(db.String(50))
    
    #there are more infos,but i only  write the above as a example
    def __init__(self,service_name,server_type,phycpu_count,mem_size,disk_info):
        self.service_name=service_name
        self.server_type=server_type
        self.phycpu_count=phycpu_count
        self.mem_size=mem_size
        self.disk_info=disk_info
    def __repr__(self):
        return "server hardware info %r,%r" %(self.service_name,server_type)

class IDC(db.Model):
    __tablename__="idc"
    idc_id=db.Column(db.Integer,primary_key=True)
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

    server_id=db.Column(db.Integer,primary_key=True)

    hostname=db.Column(db.String(10),index=True)
    #eg eth0#10.210.71.145;eth1#10.210.71.144
    ip_addr=db.Column(db.String(32))

    idc_id=db.Column(db.Integer,db.ForeignKey('idc.idc_id'))
    hardware_id=db.Column(db.Integer,db.ForeignKey('hardware.hardware_id'))
    service_id=db.Column(db.Integer,db.ForeignKey('service.service_id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'))
    
    #os_info eg: linux2.6.6 win8.0.0 or others
    os_info=db.Column(db.String(50))


    def __init__(self,hostname,ip_addr,idc_id,hardware_id,service_id,user_id,os_info):
        self.hostname=hostname
        self.ip_addr=ip_addr
        self.idc_id=idc_id
        self.hardware_id=hardware_id
        self.service_id=service_id
        self.user_id=user_id
        self.os_info=os_info

    def __repr__(self):
        return  "service info: hostname:%r" % self.hostname

