from models.user import UserModel

# In memory database for storing userid and password.
# users = [
#     User(1, "admin", "ADPadp@1212")
# ]

# username_mapping={
#     'admin':{
#         'id' = 1,
#         'username' = 'admin',
#         'password' = 'ADPadp@1212'
#     }
# }
'''
Mapping which aalows user details to be retrieved by id and username
'''
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# userid_mapping={
#     1: {
#         'id' = 1,
#         'username' = 'admin',
#         'password' = 'ADPadp@1212'
#     }
# }

''' when user authenticate using /auth and send username and password. username and password is passed to authenticate()
we retrieve user details of passed user from username_mapping dictionary and compare user password with passed password.
if they match we assume everying is right and we return user which is use to generate JWT token
'''


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = UserModel.find_by_user(username)
    if user and (user.password == password):
        return user


'''
The identity function is unqiue to Flask JWT extension, whenever they request an endpoint where authentication need to 
be done, we use identity method. Identity function takes payload, Payload is content of JWT token.
and from identity function we get the identity which is the userid, from userid we can extract user details using 
userid_mapping dictionary.
'''


def identity(payload):
    user_id = payload['identity']
    # return userid_mapping.get(user_id,None)
    return UserModel.find_by_id(user_id)
