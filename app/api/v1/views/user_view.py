import random
from flask import Flask, request, jsonify,Blueprint
import re
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from ..models import user_model



user_blu = Blueprint('user_blu', __name__,url_prefix='/api/v1/auth')

user_object = user_model.Users()


@user_blu.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}) 
    username = data.get('username').strip()
    password = data.get('password').strip()
    #confirm_password = data.get('confirm_password').strip()
    role=data.get('role').strip()

    if username is None or not username:
        return jsonify({"message": "Username is required, specify"}),206
    if role is None or not role:
        return jsonify({"message":"Role is required, specify"}),206
    if len(password) < 5:
        return jsonify({"message": "Password entered too short, min 5 characters"}),206
    #if confirm_password != password:
        #return jsonify({"message": "Password mismatch, please check"}) 
    response = jsonify(user_object.put(username,password,role))
    response.status_code = 201
    return response

@user_blu.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}),400 
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Invalid username or password"}), 400
    validate_ = user_object.password_check(username, password)
    user=user_object.get_user_by_username(username)
    if validate_ == "Validated":
        access_token = create_access_token(identity=user)
        return jsonify(dict(token = access_token, message = "Logged in, welcome")), 200
    response = jsonify(validate_)
    response.status_code = 401
    return response

@user_blu.route('attendants',methods=['GET'])
def get_all_users():
    response=jsonify(user_object.get_all_users())
    response.status_code=200
    return response

    
    