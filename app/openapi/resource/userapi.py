from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse
from flask.ext.restful import marshal_with,fields
import json


user_info={
    'id': fields.Integer,
    'service_id':fields.Integer,
    'username': fields.String,
    'password': fields.String,
}

class user(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('service_id',type=int)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        user_info = parser.parse_args()
        username=user_info.username
        password=user_info.password
        service_id=user_info.service_id
        try:
            user = User(username,password,service_id)
            db.session.add(user)
            status=db.session.commit()
            msg="succ"
        except:
            msg="error"

        return (jsonify({"msg":msg}))

    @marshal_with(user_info)
    def get(self,id):
        user = User.query.get(id)
        if user :
            return user
        else:
            abort(400)

    def put(self,id):

        user=User.query.get(id)
        if not user:
            return (jsonify({"msg":"user not exist"})),200

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('service_id', type=str)
        user_info = parser.parse_args()

        if user_info.username is not None:
            user.set_username(user_info.username)
        if user_info.password is not None:
            user.set_password(user_info.password)
        if user_info.service_id is not None:
            user.set_service_id(user_info.service_id)
        db.session.commit()
        return (jsonify({"msg":"modify User success"}))

    def delete(self,id):
        user = User.query.get(id)
        if not user:
            abort(400)
        else:
            db.session.delete(user)
        return jsonify({'msg':"delete "+user.username+" ok"})

class userlist(restful.Resource):
    @marshal_with(user_info)
    def get(self):
        users=db.session.query(User).all()
        return users
