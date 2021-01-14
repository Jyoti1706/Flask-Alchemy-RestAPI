from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')  # Many to one relatioship: a store can have

    def __init__(self, name):
        self.name = name

    def json(self):
        '''
        for lazy = dynamic implies that python will look into item for each store once get is called.. if we do not
        specify lazy=dynamic, at the time of running python will check item table and build a relation ship between
        store and  item and store data in list. but if large no of item are associated with each store so loading will
        take huge time and if get is not called then it will be a waste but if get is going to be called again n again
        then it is better to use without dynamic. so there is trade off.

        '''
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_store_name(cls, name):
        return cls.query.filter_by(name=name).first()  # fetch first row where name = name

    def save_to_db(self):
        db.session.add(self)  # inserting data to DB
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
