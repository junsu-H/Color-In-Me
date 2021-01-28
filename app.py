from flask import Flask
from flask_restx import Resource, Api
from face_detection import FaceDetection

app = Flask(__name__)
api = Api(app)

# FaceDetection - face_detection.py에서 namespace, 
# /face-detection - URL (localhost:5000/face-detection)
api.add_namespace(FaceDetection, '/face-detection')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)