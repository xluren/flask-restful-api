flask-restful-api
=================

flask restful api demo 

This demo  should thanks to   

1. the [paper](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) about restful 

2. the [flask-restful](https://github.com/twilio/flask-restful/) the flask package

3. [REST-auth](https://github.com/miguelgrinberg/REST-auth) the demo without flask-restful


from this demo ,i want to simulate the struct of twitter.com,and it shows how  will i design the twitter's struct

i split twitter's struct  into two levels 

1. the openapi levels

2. the app levels


the openapi level only offer api ,the api return type  is  json 

the app levels use the json which openapi return ,the app levels may be a website or an android app or an ios app


@2014-10-27 

the demo include Three api

POST /v1/user/      add a user 

GET  /v1/user/id    get a user

DELETE /va/user/id  DELETE a user

how to test

POST a  user like this
```
[xluren@test ~]$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"xluren","password":"jasmine"}' http://10.210.71.145:9998/v1/user
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 49
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:34:24 GMT

{
      "msg": "add User success", 
            "status": 200
}[xluren@test ~]$
```

GET a user like this
```
[xluren@test ~]$ curl -i -X GET http://10.210.71.145:9998/v1/user/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:35:27 GMT

{
      "username": "migue1"
}[xluren@test ~]$ curl -i -X GET http://10.210.71.145:9998/v1/user/3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:35:29 GMT

{
      "username": "xluren"
}[xluren@test ~]$ 
```
DELETE a user like this 
```
[xluren@test ~]$ curl -i -X DELETE  http://10.210.71.145:9998/v1/user/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 48
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:36:07 GMT

{
      "msg": "delete migue ok", 
            "status": 200
}[xluren@test ~]$ curl -i -X DELETE  http://10.210.71.145:9998/v1/user/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 49
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:36:09 GMT

{
      "msg": "delete migue1 ok", 
            "status": 200
}[xluren@test ~]$ curl -i -X DELETE  http://10.210.71.145:9998/v1/user/3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 49
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:36:11 GMT

{
      "msg": "delete xluren ok", 
            "status": 200
}[xluren@test ~]$ curl -i -X DELETE  http://10.210.71.145:9998/v1/user/4
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 53
Server: Werkzeug/0.9.6 Python/2.6.6
Date: Mon, 27 Oct 2014 05:36:13 GMT

{
        "message": "Bad Request", 
                "status": 400
}
[xluren@test ~]$
```

