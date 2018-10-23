from flask_restful import Resource, reqparse
from flask import Flask, jsonify, request
from flask_jwt import jwt_required


all_products = []

all_sales = []


class ProductResource(Resource):
	@jwt_required()
	def post(self):
		data = request.get_json()
		_id = len(all_products)+1
		prod_name = data['prod_name']

		product_payload = {"_id":_id,"prod_name":data["prod_name"],"price":data["price"],"category":data["category"],"description":data["description"],"stock":data["stock"],"min_stock":data["min_stock"]}
		all_products.append(product_payload)
		return all_products, 201
		return {"message":'Product : {} added successfully'.format(prod_name)}, 201

	def get(self):
		return {"Products Available":all_products}, 200

class ProductDeletebyName(Resource):
	def delete(self, prod_name):
		global all_products
		all_products = [product for product in all_products if product["prod_name"] != prod_name]
		return "{} is deleted.".format(prod_name), 200		

class ProductById(Resource):
	def put(self, _id):
		data = request.get_json()
		#_id = len(all_products)+1
		prod_name = data['prod_name']
		parser = reqparse.RequestParser()
		parser.add_argument("prod_name")
		parser.add_argument("price")
		parser.add_argument("category")
		parser.add_argument("description")
		parser.add_argument("stock")
		parser.add_argument("min_stock")
		args = parser.parse_args()

		for product in all_products:
			if(_id == product["_id"]):
				product['prod_name'] = args['prod_name']
				product["price"] = args["price"]
				product["category"] = args["category"]
				product["description"] = args["description"]
				product["stock"] = args["stock"]
				product["min_stock"] = args["min_stock"]
				return product, 200
		product = {
			"_id":_id,
			"prod_name": prod_name,
			"price": args["price"],
			"category": args["category"],
			"description": args["description"],
			"stock": args["stock"],
			"min_stock": args["min_stock"]
		}
		all_products.append(product)
		return product, 201
		return {"message":'Product : {} updated'.format(prod_name)}, 201

	def get(self, _id):
		for product in all_products:
			if product['_id'] == _id:
				return product
		return {'Product': None}, 404

class SaleResource(Resource):
	@jwt_required()
	def post(self):
		data = request.get_json()
		sale_id = len(all_sales)+1
		
		sale_payload = {"sale_id":sale_id,"product":data["product"],"price":data["price"],"quantity":data["quantity"],"total_amt":data["total_amt"],"attendant":data["attendant"]}
		all_sales.append(sale_payload)
		return {"Sale created":sale_payload}, 201

	@jwt_required()
	def get(self):
		return {"message":all_sales}, 200

class SaleById(Resource):
	@jwt_required()
	def get(self, sale_id):
		for sale in all_sales:
			if sale["sale_id"] == sale_id:
				return sale
		return {'Sale': None}, 404

	def delete(self, sale_id):
		global all_sales
		all_sales = [sale for sale in all_sales if sale["sale_id"] != sale_id]
		return "sale ID :{} has been deleted.".format(sale_id), 200		
