from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse
from flask.ext.restful import marshal_with,fields


user_info={
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
}

class user(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        user_info = parser.parse_args()
        username=user_info.username
        password=user_info.password

        if User.query.filter_by(username=username).first() is not None:
            return (jsonify({"msg":"user exist"}))
        else:
            user = User(username,password)
        db.session.add(user)
        status=db.session.commit()
        return (jsonify({"msg":"add user successful"}))

    @marshal_with(user_info)
    def get(self,id):
        user = User.query.get(id)
        if user :
            return user
        else:
            abort(400)

    def put(self,id):

        if not User.query.get(id):
            return (jsonify({"msg":"user not exist"})),200

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        user_info = parser.parse_args()
        username=user_info.username
        password=user_info.password

        user=User.query.get(id)
        user.set_username(username)
        user.set_password(password)
        print user.username
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
