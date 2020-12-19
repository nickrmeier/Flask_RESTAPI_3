from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from secret import key
from resources.user import UserRegister
from resources.item import Item, ItemsList

app = Flask(__name__)
api = Api(app)
app.secret_key = key
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemsList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == '__main__':  
    app.run(port=5000, debug=True)
