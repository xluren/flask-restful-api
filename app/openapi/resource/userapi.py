from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse

class userapi(restful.Resource):
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

    def get(self,id):
        user = User.query.get(id)
        if not user:
            abort(400)
        return jsonify({'username': user.username})

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        user_info = parser.parse_args()
        username=user_info.username
        password=user_info.password

        if User.query.filter_by(username=username).first() is  None:
            return (jsonify({"msg":"user not exists"}))
            
        user_list=db.session.query(User).filter_by(username=username).all()
        print len(user_list)
        user=user_list[0]
        
        user.hash_password(password)
        db.session.commit()
        return (jsonify({"status":200,"msg":"modify User success"}))

    def delete(self,id):
        user = User.query.get(id)
        if not user:
            abort(400)
        else:
            db.session.delete(user)
        return jsonify({'status':200, 'msg':"delete "+user.username+" ok"})
