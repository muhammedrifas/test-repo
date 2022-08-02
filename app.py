from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList

# from models.item import ItemModel
# from models.user import UserModel

app = Flask(__name__)
app.secret_key = 'my_secret_key'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=6000)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

db.init_app(app)
app.run(port=5000)
