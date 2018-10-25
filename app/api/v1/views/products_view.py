from flask import Flask, Blueprint, request, jsonify,json
from flask_jwt_extended import (JWTManager, get_jwt_claims, jwt_required)
from ..models import product_model
from ..models.product_model import products_object

product_blu = Blueprint('product_blu', __name__,url_prefix='/api/v1')


product_object = product_model.Product()

@product_blu.route('/products',methods=['POST'])
@jwt_required
def post_product():
    data=request.get_json()
    if not data:
        return jsonify({"message": 'Empty fields not allowed'}) 
 
    prod_id=len(products_object)
    prod_name=data.get("prod_name")
    category=data.get("category")
    price=data.get("price")
    stock=data.get("stock")
    min_stock=data.get("min_stock")
    description=data.get("description")

    if prod_name is None or not prod_name:
        return jsonify({"message":"Product name required"}),206
    if min_stock is None or not min_stock:
        return jsonify({"message":"Product min_stock required"}),206
    if stock is None or not stock:
        return jsonify({"message":"Product inventory required"}),206
    if price is None or not price:
        return jsonify({"message":"You must specify the product price"}),206
    claims=get_jwt_claims()
    admin="admin"
    if claims['role'] != admin:
        return jsonify({"message":"Admin login required"}),401
    response=jsonify(product_object.put(prod_id, prod_name, category, price,stock,min_stock,description))

    response.status_code = 201
    return response  
@product_blu.route('/products',methods=['GET']) 
@jwt_required
def get_all_products():
    response=jsonify(product_object.get_all_products())
    response.status_code=200
    return response
@product_blu.route('/products/<int:prod_id>',methods=['GET']) 
@jwt_required
def get_product_by_id(prod_id):
    response=jsonify(product_object.get_product_by_id(prod_id))
    response.status_code=200
    return response
