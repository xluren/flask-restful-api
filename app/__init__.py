from flask import Flask
from flask.ext.sqlalchemy  import SQLAlchemy
from flask.ext import restful

app = Flask(__name__)
app.config.from_object('config.TestConfig')
db=SQLAlchemy(app)

api = restful.Api(app)
from app.openapi.resource.userapi import userapi
api.add_resource(userapi, '/v1/user','/v1/user/<int:id>')

db.create_all()
