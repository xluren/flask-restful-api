from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort

class userapi(restful.Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            print "hello"
            abort(400)    # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            print "world"
            abort(400)    # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return (jsonify({"status":200,"msg":"add User success"}))
    def get(self,id):
        print id
        user = User.query.get(id)
        if not user:
            abort(400)
        return jsonify({'username': user.username})
