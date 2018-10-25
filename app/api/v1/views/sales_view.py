import datetime
from flask import Flask, Blueprint, request, jsonify,json
from flask_jwt_extended import (JWTManager, get_jwt_claims,get_jwt_identity, jwt_required)
from ..models import sales_model

from ..models.sales_model import sales_dbs


sale_blu = Blueprint('sale_blu', __name__,url_prefix='/api/v1')

#sales dbs is the data structure for our sales model

sale_object = sales_model.Sale()

@sale_blu.route('/sales',methods=['POST'])
@jwt_required
def post_sales():
	data=request.get_json()
	sale_id=len(sales_dbs)
	product=data.get("product")
	price=data.get("price")
	quantity=data.get("quantity")
	total_amnt=data.get("total_amnt")
	attendant=get_jwt_identity()
	now = datetime.datetime.now()
	date=now

	if quantity is None or not quantity:
		return jsonify({"message": "Enter the items count"}),206
	if total_amnt is None or not total_amnt:
		return jsonify({"message":"Enter total amount in this sale"}),206
	claims = get_jwt_claims()
	attendant="attendant"
	if claims["role"] != attendant:
		return jsonify({"message":"User login required"}),401
	response=jsonify(sale_object.put(sale_id, product, price,quantity,total_amnt,attendant, date))
	response.status_code=201
	return response

@sale_blu.route('/sales',methods=['GET'])
@jwt_required
def get_all_sales():
	claims=get_jwt_claims()
	admin="admin"
	if claims["role"]!= admin:
		return jsonify({"message":"Only an admin can view all sales records"}),401
	response= jsonify(sale_object.get_all_sales())
	response.status_code=200
	return response
@sale_blu.route('/sales/<int:sale_id>',methods=['GET'])
@jwt_required
def get_sale_by_id(sale_id):
	claims=get_jwt_claims()
	identity=get_jwt_identity()
	admin="admin"
	if claims["role"]!= admin and sales_dbs[sale_id]["attendant"]!=identity:
		return jsonify({"message":"Only an admin or attendant who created this sale are allowed to view it"}),401
	response=jsonify(sale_object.get_sale_by_id(sale_id))
	response.status_code=200
	return response
	





