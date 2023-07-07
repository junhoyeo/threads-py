from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "zuck"
post_id = "3140957200974444958"
thread = api.get_user_profile_thread(username, post_id=post_id)
print(thread)
