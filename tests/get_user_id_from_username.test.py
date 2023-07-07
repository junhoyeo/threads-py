from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "_junhoyeo"
user_id = api.get_user_id_from_username(username)
print(user_id)
