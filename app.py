from main import ThreadsAPI

api = ThreadsAPI()
username = "stkildafc"

user_id = api.get_user_id_from_username(username)
user_profile = api.get_user_profile(username)
user_threads = api.get_user_profile_threads(username)

print(user_id)
print("\n", user_profile)
print("\n", user_threads)