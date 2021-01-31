from flask import Flask
from flask_restx import Resource, Api
import face_detection 
import os
from hello import Hello

app = Flask(__name__)
api = Api(app)
api.add_namespace(Hello, '/hello')

# Directory Setting
app.config['UPLOADED_PATH'] = os.path.join(app.root_path, 'static')

# Allow file Setting
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)