import datetime

sales_dbs={}

class Sale():
	def __init__(self):

		self.sales_dbs = {}
		
	def put(self,sale_id, product, price,quantity,total_amnt,attendant, date):
		self.sale_detail={}
		self.sale_detail["sale_id"]=sale_id
		self.sale_detail["product"]=product
		self.sale_detail["price"]=price
		self.sale_detail["quantity"]=quantity
		self.sale_detail["total_amnt"]=total_amnt
		self.sale_detail["attendant"]=attendant
		self.sale_detail["date"]=date

		sales_dbs[sale_id]=self.sale_detail
		return {"message":"Sale record added"}
	def get_all_sales(self):
		return sales_dbs
	def get_sale_by_id(self,sale_id):
		if sale_id in sales_dbs:
			return sales_dbs[sale_id]
		return{"message":"No such record found"}