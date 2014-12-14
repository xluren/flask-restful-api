from flask import Flask
from flask.ext.sqlalchemy  import SQLAlchemy
from flask.ext import restful

app = Flask(__name__)
app.config.from_object('config.MysqlConfig')
db=SQLAlchemy(app)

api = restful.Api(app)
from app.openapi.resource.userapi import user,userlist

api.add_resource(user, '/v1/user','/v1/user/<int:id>')
api.add_resource(userlist, '/v1/user','/v1/userlist')

db.create_all()
