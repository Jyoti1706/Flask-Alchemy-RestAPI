from flask import Flask
from flask_restful import Api
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False  # to stop tracking sql alchemy.
app.secret_key = 'Secretiskey'
api = Api(app)


@app.before_first_request  # this will create all the table in data.db
def create_tables():
    db.create_all()


''' 
here with jwt, we are creating endpoint '/auth'. here we will pass username and password and authentication key will be 
generated. and latter will be used to identify the call.
'''
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/stores/<string:name>')

'''
Generally when we run a import statement it will run all the classes and methods in it. so here if we import app for 
some data in some other py file.run statement will run and app will be launched in port 5000. so to make sure the launch
works only when app.py file is run directly we use "if __name__ == '__main__':" as when python runs a file, then it 
assign main name to the file. so we can check file name and we can run accordingly.
'''
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
