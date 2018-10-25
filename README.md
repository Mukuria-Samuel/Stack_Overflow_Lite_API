https://travis-ci.org/Mukuria-Samuel/Store_Manager_app.svg?branch=ch_app_on_heroku

[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

**Creator**: s mukuria


#Store Manager#
Store manager app is a web application that helps store owners manage sales and product inventory records.

Endpoints:
   	http://127.0.0.1:5000/api/v1/auth/register 		|	register a user
   	
   	http://127.0.0.1:5000/api/v1/auth/login 		|	login a user
   	
   
   	http://127.0.0.1:5000/api/v1/attendants 		|	get all users
   	
   	http://127.0.0.1:5000/api/v1/products 			|	post a product
   
   	http://127.0.0.1:5000/api/v1/products	 		|	get all products
	
	http://127.0.0.1:5000/api/v1/products/<int:prod_id>		|	get a single product
   	
   
   	http://127.0.0.1:5000/api/v1/sales 						|	post a sale
   	
   	http://127.0.0.1:5000/api/v1/sales/<int:sale_id> 		|	get all sales
   	
   	http://127.0.0.1:5000/api/v1/sales/<int:sale_id> 		|	get a single sale
   
 
 **Python Versions**: 3.6+ only
 
 ## Getting Started
 
 Navigate to a directory that you want to work in and clone down this repository.
 
 ```
 $ git clone https://github.com/Store_Manager_app/app.git
 ```
 
 ### For Development
 
 Move into the cloned directory and start a new Python 3 [virtual environment](https://docs.python.org/3/tutorial/venv.html). You should be using Python 3.6 or later.
 
 ```
 $ cd pyramid
 pyramid $ python3 -m venv ENV
 (ENV) flask $ source ENV/bin/activate
 ```
 
 ```
 (ENV) flask $ pip install -r requirements.txt
 ```
 
 In order to run the application, type `flask run`.
 If all your stuff is configured properly, your development server should be running on port 5000.
 
 ### For Deployment (Heroku)
 
