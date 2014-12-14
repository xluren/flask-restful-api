from app import db
from app.openapi.db_model.models import User
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse
from flask.ext.restful import marshal_with,fields
import json


hardware_info={
    'id': fields.Integer,
    'server_name':fields.String,
    'server_type': fields.String,
    'phycpu_count': fields.Integer,
    'mem_size':fields.Integer,
    'disk_size':fields.Integer,
}

class hardware(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hardware_name',type=str,required=True)
        parser.add_argument('hardware_type', type=str,required=True)

        parser.add_argument('phycpu_count', type=int, required=True)
        parser.add_argument('mem_size', type=int, required=True)
        parser.add_argument('disk_size', type=int, required=True)
        
        hardware_info = parser.parse_args()
        try:
            hardware = Hardware(hardware.hardware_name,
                            hardware.hardware_type,
                            hardware.phycpu_count,
                            hardware.mem_size,
                            hardware.disk_size)
            db.session.add(hardware)
            status=db.session.commit()
            msg="succ"
        except:
            msg="error"

        return (jsonify({"msg":msg}))

    @marshal_with(hardware_info)
    def get(self,id):
        hardware = Hardware.query.get(id)
        if hardware :
            return hardware
        else:
            abort(400)

    def put(self,id):

        Hardware.query.filter_by(hardware_id=id).update(request.json)
        db.session.commit()
        return (jsonify({"msg":"modify hardware  success"}))

    def delete(self,id):
        hardware = Hardware.query.get(id)
        if not hardware:
            abort(400)
        else:
            db.session.delete(hardware)
        return jsonify({'msg':"delete "+hardware.server_name+" ok"})

class hardwarelist(restful.Resource):
    @marshal_with(hardware_info)
    def get(self):
        hardwares=db.session.query(Hardware).all()
        return hardwares
