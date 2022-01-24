from flask import Flask, jsonify, request, send_file, render_template, Response
from flask_cors import CORS
import argparse
import os
from service import service
from config import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify('test message')

@app.route('/api/signup', methods=['POST'])
def signup():
    usertype = request.json['usertype']
    username = request.json['username']
    password = request.json['password']
    print(usertype, username, password)
    return service.signup(usertype, username, password)

@app.route('/api/signin', methods=['POST'])
def signin():
    username = request.json['username']
    password = request.json['password']
    print(username, password)
    return service.signin(username, password)

@app.route('/api/getusertype', methods=['POST'])
def getUsertype():
    username = request.json['username']
    return service.getUsertype(username)

@app.route('/api/setpatientinfo', methods=['POST'])
def setPatientInfo():
    username = request.json['username']
    name = request.json['name']
    birth = request.json['birth']
    tel = request.json['tel']
    intro = request.json['intro']
    return service.setPatientInfo(username, name, birth, tel, intro)

@app.route('/api/getpatientinfo', methods=['POST'])
def getPatientInfo():
    username = request.json['username']
    return service.getPatientInfo(username)

@app.route('/api/setdoctorinfo', methods=['POST'])
def setDoctorInfo():
    username = request.json['username']
    name = request.json['name']
    birth = request.json['birth']
    tel = request.json['tel']
    intro = request.json['intro']
    return service.setDoctorInfo(username, name, birth, tel, intro)

@app.route('/api/getdoctorinfo', methods=['POST'])
def getDoctorInfo():
    username = request.json['username']
    return service.getDoctorInfo(username)

@app.route('/api/getavatar', methods=['POST'])
def getAvatar():
    username = request.json['username']
    return service.getAvatar(username)

@app.route('/api/setavatar', methods=['POST'])
def setAvatar():
    print(request)
    username = request.headers['username']
    file = request.files[username]
    return service.setAvatar(username, file)

@app.route("/data/images/avatars/<imageFilename>")
def getAvaterImage(imageFilename):
    with open(os.path.join(IMAGE_AVATAR_DIR, imageFilename), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image")
        return resp

@app.route("/data/images/medical/<imageFilename>")
def getMedicalImage(imageFilename):
    with open(os.path.join(IMAGE_MEDICAL_DIR, imageFilename), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image")
        return resp

@app.route('/api/setmedicalimage', methods=['POST'])
def setMedicalImage():
    print(request)
    username = request.headers['username']
    file = request.files[username]
    return service.setMedicalImage(username, file)

@app.route('/api/getmedicalimages', methods=['POST'])
def getMedicalImages():
    username = request.json['username']
    return service.getMedicalImages(username)

@app.route('/api/getalldoctorusername', methods=['GET'])
def getAllDoctorUsername():
    return service.getAllDoctorUsername()


def main():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--data_path", type=str, default='')
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5005)
    args = parser.parse_args()

    app.run(port=args.port, host=args.host, threaded=True, debug=False)

if __name__ == "__main__":
    main()