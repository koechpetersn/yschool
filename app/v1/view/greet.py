
from flask_restful import Resource
from flask import render_template,Response,request,flash,redirect,url_for

class GreetUs(Resource):
    def get(self):
        ourname = "Paul"
        return Response(render_template("example.html",name=ourname))