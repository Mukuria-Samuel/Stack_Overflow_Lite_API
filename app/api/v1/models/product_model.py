import os

products_object={}

class Product():
	def put(self,prod_id,prod_name,category,price,stock,min_stock,description):
		
		self.prod_detail={}
		if prod_id in products_object:
			return {"message":"{} : Added".format(prod_name)}
		self.prod_detail["prod_id"]=prod_id
		self.prod_detail["prod_name"]=prod_name
		self.prod_detail["category"]=category
		self.prod_detail["price"]=price
		self.prod_detail["stock"]=stock
		self.prod_detail["min_stock"]=min_stock
		self.prod_detail["description"]=description
		products_object[prod_id]=self.prod_detail
		return {"message":" {} : Added".format(prod_name)}
	def get_all_products(self):
		return products_object

	def get_product_by_id(self, prod_id):
		print(products_object)
		if prod_id in products_object:
			return products_object[prod_id]
		return{"message":"No such product in inventory"}



