from flask.ext import restful
from flask import Flask, abort, request, jsonify, g, url_for
app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def post(self):
        print request.json.get('username')        
        print request.json.get('password')        
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=10000)
