from flask import request
from flask_restx import Resource, Api, Namespace

Hello = Namespace('Hello')

@Hello.route('', methods=['GET', 'POST'])
class HelloPost(Resource):
    def get(self):
        return {
            "hello": "world!"
        }