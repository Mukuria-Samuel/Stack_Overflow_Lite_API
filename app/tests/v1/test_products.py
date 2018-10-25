import json
from .base_test import BaseTestCase
class TestProducts(BaseTestCase):

	def test_post_product(self):
#Register admin, then log him in inorder to post a product..
		with self.client:
			self.client.post('/api/v1/auth/register',data=json.dumps(dict(username='adminman',password='summertime1',role='admin',confirm_password='summertime1')),
				content_type='application/json')
			login_response = self.client.post('/api/v1/auth/login',data=json.dumps(dict(username='adminman',password='summertime1')),content_type='application/json')
			
			result=json.loads(login_response.data)
			token=result["token"]
			response = self.client.post('/api/v1/products',headers=dict(Authorization="Bearer " + token),
				data=json.dumps(dict(
					prod_id=2,
					prod_name='inifinix',
					category='PHONE',
					price=15000,
					stock=20,
					min_stock=5,
					description='4G/dual simcard')),content_type='application/json')

			response_data = json.loads(response.data)
			self.assertEqual("inifinix : Added",response_data["message"])
			self.assertEqual(response.status_code, 201)

	def test_get_all_products(self):
		with self.client:
			self.client.post('/api/v1/auth/register',data=json.dumps(dict(
					username='userman',
					password='summertime2',
					role='attendant',
					confirm_password='summertime2')),content_type='application/json')
		
			login_response = self.client.post('/api/v1/auth/login',data=json.dumps(dict(
					username='userman',
					password='summertime2')),content_type='application/json')
			result=json.loads(login_response.data)
			token=result["token"]
			response = self.client.get('/api/v1/products',headers=dict(Authorization="Bearer " + token))
			self.assertEqual(response.status_code, 200)

	def test_get_product_by_id(self):
		with self.client:self.client.post('/api/v1/auth/register',data=json.dumps(dict(
					username='adminman',
					password='summertime1',
					role='admin',
					confirm_password='summertime1'
				)),content_type='application/json')
		login_response = self.client.post('/api/v1/auth/login',data=json.dumps(dict(
					username='adminman',
					password='summertime1')),content_type='application/json')
		result=json.loads(login_response.data)
		token=result["token"]
		self.client.post('/api/v1/products',headers=dict(Authorization="Bearer " + token),
				data=json.dumps(dict(
					prod_id=2,
					prod_name='inifinix',
					category='PHONE',
					price=15000,
					stock=20,
					min_stock=5,
					description='4G/dual simcard')),content_type='application/json')
		response = self.client.get('/api/v1/products/2',headers=dict(Authorization="Bearer " + token))
		self.assertEqual(response.status_code, 200)
	
