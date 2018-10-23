from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from api.user_security import authenticate, identity
from api.resources import ProductResource, ProductById, SaleResource, SaleById, ProductDeletebyName

def create_app(env="dev"):
    app = Flask(__name__)
    app.secret_key = 'ourlitlesecret'
    api = Api(app)

    jwt = JWT(app, authenticate, identity)

    api.add_resource(ProductResource,'/api/v1/products')
    api.add_resource(ProductById,'/api/v1/products/<int:_id>')
    api.add_resource(ProductDeletebyName,'/api/v1/products/<string:prod_name>')
    api.add_resource(SaleResource,'/api/v1/sales')
    api.add_resource(SaleById,'/api/v1/sales/<int:sale_id>')

    return app
