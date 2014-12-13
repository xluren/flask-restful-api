from app import db
from app.openapi.db_model.models import Service
from flask.ext import restful
from flask     import request,jsonify,abort
from flask.ext.restful import reqparse
from flask.ext.restful import marshal_with,fields


service_info={
    'service_id': fields.Integer,
    'service_name': fields.String,
    'serive_parent': fields.Integer
}

class Service(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('service_name', type=str, required=True)
        parser.add_argument('serive_parent', type=int, required=True)
        service_info = parser.parse_args()
        service_name=service_info.service_name
        serive_parent=service_info.serive_parent

        if Service.query.filter_by(service_id=serive_parent).first() is  None:
            return (jsonify({"msg":"no such parent"}))
        elif Service.query.filter_by(service_id=service_id).first() is not None:
            return (jsonify({"msg":"service exists"}))
        else:
            service = Service(service_name,serive_parent)
        db.session.add(service)
        status=db.session.commit()
        return (jsonify({"msg":"add user successful"}))

    @marshal_with(user_info)
    def get(self,id):
        service = Service.query.get(id)
        if service :
            return service
        else:
            abort(400)

    def put(self,id):

        if not Service.query.get(id):
            return (jsonify({"msg":"user not exist"})),200

        parser = reqparse.RequestParser()
        parser.add_argument('service_name', type=str, required=True)
        parser.add_argument('serive_parent', type=int, required=True)
        service_info = parser.parse_args()
        service_name=service_info.service_name
        serive_parent=service_info.serive_parent

        service=Service.query.get(id)
        service.set_service_name(service_name)
        service.set_service_parent(service_parent)
        db.session.commit()
        return (jsonify({"msg":"modify serice success"}))

    def delete(self,id):
        service = Service.query.get(id)
        if not service:
            abort(400)
        else:
            db.session.delete(service)
        return jsonify({'msg':"delete  service ok"})

class servicelist(restful.Resource):
    @marshal_with(service_info)
    def get(self):
        services=db.session.query(Service).all()
        return services
