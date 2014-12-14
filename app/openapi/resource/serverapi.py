from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse
from flask.ext.restful import marshal_with,fields
import json


server_info={
    'id': fields.Integer,
    'service_id':fields.Integer,
    'username': fields.String,
    'password': fields.String,
}

class server(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hostname',type=str,required=True)
        parser.add_argument('ip_addr', type=str,required=True)

        parser.add_argument('hardware_id', type=int, required=True)
        parser.add_argument('idc_id', type=int, required=True)
        parser.add_argument('service_id', type=int, required=True)
        parser.add_argument('user_id', type=int, required=True)
        
        parser.add_argument('os_info', type=str, required=True)

        service_id=server_info.service_id
        try:
            server = Server(server_info.hostname,
                            server_info.ip_addr,
                            server_info.hardware_id,
                            server_info.idc_id,
                            server_info.service_id,
                            server_info.user_id,
                            server_info.os_info)
            db.session.add(server)
            status=db.session.commit()
            msg="succ"
        except:
            msg="error"

        return (jsonify({"msg":msg}))

    @marshal_with(server_info)
    def get(self,id):
        server = User.query.get(id)
        if server :
            return server
        else:
            abort(400)

    def put(self,id):

        Server.query.filter_by(service_id=id).update(request.json)
        db.session.commit()
        return (jsonify({"msg":"modify server  success"}))

    def delete(self,id):
        Server = Server.query.get(id)
        if not Server:
            abort(400)
        else:
            db.session.delete(Server)
        return jsonify({'msg':"delete "+Server.hostname+" ok"})

class serverlist(restful.Resource):
    @marshal_with(server_info)
    def get(self):
        servers=db.session.query(Server).all()
        return servers
