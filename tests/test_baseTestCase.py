import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import json
from unittest import TestCase

from app import create_app


class BaseTestCase(TestCase):

	def setUp(self):
		"""Configure test enviroment."""
		os.environ['APP_SETTINGS'] = 'Testing'
		self.app = create_app("Testing")
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def tearDown(self):
		#self.app_context.pop()
		pass

class ProductResourceTestCase(BaseTestCase):
	def setUp(self):
		self.app = create_app("Testing")
		self.client = self.app.test_client()

		self.create_product = json.dumps(dict(
			_id= 1,
			prod_name ='infinix',
			price=12000,
			category='Phone',
			description='interesting phone',
			stock=20,
			min_stock=5))

		self.client.post('/api/v1/products', data=self.create_product, content_type='application/json')

	def test_post_product(self):
		result = self.client.post('/api/v1/products', data=self.create_product, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 201)
		self.assertEqual(result.content_type, 'application/json')

	def test_get_product(self):
		result = self.client.get('/api/v1/products', data=self.create_product, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.content_type, 'application/json')

	def test_get_product_by_id(self):
		self.client.post('/api/v1/products', data=self.create_product, content_type='application/json')
		result = self.client.get('/api/v1/products/1', data=self.create_product, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.content_type, 'application/json')

class SaleResourceTestCase(BaseTestCase):
	def setUp(self):
		self.app = create_app("Testing")
		self.client = self.app.test_client()

		self.create_sale = json.dumps(dict(
			sale_id= 1,
			product ='infinix',
			price=12000,
			quantity=2,
			total_amt=24000,
			attendant='nancy',
			))

		self.client.post('/api/v1/sales', data=self.create_sale, content_type='application/json')

	def test_post_sale(self):
		result = self.client.post('/api/v1/sales', data=self.create_sale, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 201)
		self.assertEqual(result.content_type, 'application/json')

	def test_get_sale(self):
		result = self.client.get('/api/v1/sales', data=self.create_sale, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.content_type, 'application/json')

	def test_get_sale_by_id(self):
		result = self.client.get('/api/v1/sales/1', data=self.create_sale, content_type='application/json')
		data = json.loads(result.data.decode())
		print(data)
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.content_type, 'application/json')

