from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "iamiks"
user_id = api.get_user_id_from_username(username)
print(user_id)
threads = api.get_user_profile_threads(username, user_id=user_id)
print(threads)
