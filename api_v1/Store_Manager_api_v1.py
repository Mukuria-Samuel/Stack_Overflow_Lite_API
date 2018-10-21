# from the flask library import a class named Flask
import random
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# create an instance of the Flask class
app = Flask(__name__)
api = Api(app)



all_products = []
        
sales = []



class product_list(Resource):

	def post(self):
		data = request.get_json()
		id = len(all_products) +1
		prod_name = data['prod_name']

		products = {'id':id,"prod_name":data["prod_name"],"price":data["price"],"category":data["category"],"description":data["description"],"stock":data["stock"],"min_stock":data["min_stock"]}
		all_products.append(products)
		return {'Message':'Product : {} added successfully'.format(prod_name)}, 201
		return products
		

	def get(self):
		return jsonify({"Our inventory":all_products})

class one_product(Resource):
	def get(self, id):
		for product in all_products:
			if product['id'] == id:
				return product
		return {'Product': None}, 404

class Sale(Resource):

	def post(self):
		data = request.get_json()
		sale_id = len(sales) +1
		name = data['name']

		payload = {"sale_id":sale_id,"attendant":data["attendant"],"category":data["category"],"name":data["name"],"price":data["price"],"Quantity":data['Quantity']}
		sales.append(payload)
		return {"Sale created":payload}, 201
		

	def get(self):
		return {"All Sales":sales}, 200


class one_sale(Resource):
	def get(self, attendant):
		for sale in sales:
			if sale["attendant"] == attendant:
				return {attendant:sale}
		return {'Sale':None}, 404

api.add_resource(one_product, '/api/v1/products/<int:id>')
api.add_resource(product_list, '/api/v1/products')
api.add_resource(one_sale, '/api/v1/sales/<string:attendant>')
api.add_resource(Sale, '/api/v1/sales')

if __name__ == '__main__':
    app.run(debug=True)