import json
from .base_test import BaseTestCase

#Register user so as to post a sale
class TestSales(BaseTestCase):

    def test_post_sales(self):
        with self.client:
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant')),content_type='application/json')
        
            res_result = self.client.post('/api/v1/auth/login',
                data=json.dumps(dict(
                    username="userman",
                    password="summertime2")),content_type='application/json')
            result=json.loads(res_result.data)
           
            token=result["token"]
            response = self.client.post('/api/v1/sales',headers=dict(Authorization="Bearer " + token),
                data=json.dumps(dict(
                    sale_id=1,
                    product='inifinix',
                    price=14800,
                    quantity=1,
                    total_amnt=15000,
                    attendant='userman')),content_type='application/json')

            result_res = json.loads(response.data)
            self.assertEqual("Sale record added",result_res["message"])
            self.assertEqual(response.status_code, 201)

#Test getting a sale by ID
    def test_get_sale(self):
        with self.client:
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant')),content_type='application/json')
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='adminman',
                    password='summertime1',
                    role='admin')),content_type='application/json')

            response_user=self.client.post('/api/v1/auth/login',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2')),content_type='application/json')
            result_user=json.loads(response_user.data)
            token_user=result_user['token']
            response_admin=self.client.post('/api/v1/auth/login',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2')),content_type='application/json')
            res_admin=json.loads(response_admin.data)
          
            token_adm=res_admin["token"]
            self.client.post('/api/v1/sales',
                headers=dict(Authorization="Bearer " + token_user),
                data=json.dumps(dict(
                    sale_id=1,
                    product='inifinix',
                    price=14800,
                    quantity=1,
                    total_amnt=15000,
                    attendant='userman',)),content_type='application/json')

            res_user=self.client.get('/api/v1/sales/2',headers=dict(Authorization="Bearer " + token_user))
            self.assertEqual(res_user.status_code,200)

            res_adm=self.client.get('/api/v1/sales/2',headers=dict(Authorization="Bearer " + token_adm))
            self.assertEqual(res_adm.status_code,200)

    def test_get_sales(self):
        with self.client:
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant')),content_type='application/json')
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='adminman',
                    password='summertime1',
                    role='admin')),content_type='application/json')

            response_user=self.client.post('api/v1/auth/login',
                data=json.dumps(dict(
                    username="userman",
                    password="summertime2"
                )),content_type='application/json')

            result_user=json.loads(response_user.data)
            user_token=result_user["token"]

            response_admin=self.client.post('api/v1/auth/login',
                data=json.dumps(dict(
                    username="adminman",
                    password="summertime1")),content_type='application/json')
            res_admin=json.loads(response_admin.data)
            token_=res_admin["token"]
            
            self.client.post('/api/v1/sales',headers=dict(Authorization="Bearer " + user_token),
                data=json.dumps(dict(
                    sale_id=1,
                    product='inifinix',
                    price=14800,
                    quantity=1,
                    total_amnt=15000,
                    attendant='userman',)),content_type='application/json')
            response=self.client.get('api/v1/sales',headers=dict(Authorization="Bearer " + token_))
            self.assertEqual(response.status_code,201)

    def test_get_sale(self):
        with self.client:
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant')),content_type='application/json')
            self.client.post('/api/v1/auth/register',
                data=json.dumps(dict(
                    username='adminman',
                    password='summertime1',
                    role='admin')),content_type='application/json')

            response_user=self.client.post('/api/v1/auth/login',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2')),content_type='application/json')
            result_user=json.loads(response_user.data)
            token_user=result_user['token']
            response_admin=self.client.post('/api/v1/auth/login',
                data=json.dumps(dict(
                    username='userman',
                    password='summertime2')),content_type='application/json')
            res_admin=json.loads(response_admin.data)
          
            token_adm=res_admin["token"]
            self.client.post('/api/v1/sales',
                headers=dict(Authorization="Bearer " + token_user),
                data=json.dumps(dict(
                    sale_id=1,
                    product='inifinix',
                    price=14800,
                    quantity=1,
                    total_amnt=15000,
                    attendant='userman',)),content_type='application/json')

            res_user=self.client.get('/api/v1/sales/2',headers=dict(Authorization="Bearer " + token_user))
            self.assertEqual(res_user.status_code,200)

            res_adm=self.client.get('/api/v1/sales/2',headers=dict(Authorization="Bearer " + token_adm))
            self.assertEqual(res_adm.status_code,200)
    
    
