from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="this field should not be empty")
    parser.add_argument("store_id", type=int, required=True, help="please provide store id")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_item_name(name)
        if item:
            return item.json()

        return {"message": " item not found from items list"}, 404

    def post(self, name):
        item = ItemModel.find_by_item_name(name)
        if item:
            return {"messages": "Item already exists {}.".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'Message': "Error occurred while inserting an item"}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_item_name(name)
        if item:
            item.delete_from_db()
        return {"message": "{} item deleted from items list".format(name)}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_item_name(name)
        # item = ItemModel(name, data['price'])
        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, **data)
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
