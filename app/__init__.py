
from flask import Flask
from instance.config import app_config
from flask_jwt_extended import JWTManager
from .api.v1.views.user_view import user_blu
from .api.v1.views.products_view import product_blu
from .api.v1.views.sales_view import sale_blu

def create_app(config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True

    app.config['JWT_SECRET_KEY'] = 'ourlitlesecret'
   
    jwt = JWTManager(app)

    @jwt.user_claims_loader
    def tokenize_claims(user_object):
        return {'role': user_object['role']}

    @jwt.user_identity_loader
    def identity_check(user_object):
        print(user_object)
        return user_object["username"]

#Registering enpoint blueprints here..

    app.register_blueprint(product_blu)
    app.register_blueprint(sale_blu)
    app.register_blueprint(user_blu)
    

    return app

