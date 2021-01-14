from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_store_name(name)
        if store:
            return store.json()
        return {"Message": "Store not found"}, 404

    def post(self, name):
        store = StoreModel.find_by_store_name(name)
        if store:
            return {"Message": "Store {} already exists found".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"Message": "Internal Error"}, 500
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_store_name(name)
        if store:
            store.delete_to_db()
            return {"Message": "Successfully Deleted "}, 200
        return {"Message": "No Store found "}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
