from flask import request
from flask_restx import Resource, Api, Namespace

FaceDetection = Namespace('FaceDetection')

@FaceDetection.route('/')
class FaceDetectionGet(Resource):
    def get(self):
        return "test"