from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "iamiks"
post_id = "3140623946340547898"
thread = api.get_user_profile_thread(username, post_id=post_id)
print(thread)
