from flask_restful import Api, Resource
from flask import Blueprint

from .view.greet import GreetUs

version_one = Blueprint('api', __name__)
api = Api(version_one)

api.add_resource(GreetUs,"/greet")