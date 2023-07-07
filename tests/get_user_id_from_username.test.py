from threadspy._thread import ThreadsAPI

api = ThreadsAPI()
username = "iamiks"
user_id = api.get_user_id_from_username(username)
print(user_id)
