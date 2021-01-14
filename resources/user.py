import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Field cannot be blank")
    parser.add_argument('password', type=str, required=True, help="Field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        check_user = UserModel.find_by_user(data['username'])
        if check_user:
            return "{message: 'User already exists'}", 400
        user = UserModel(**data)
        user.save_to_db()

        return "{message: 'User created successfully'}", 201
