from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "zuck"
user_id = api.get_user_id_from_username(username)
print(user_id)
