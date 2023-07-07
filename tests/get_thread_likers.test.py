from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "zuck"
post_id = "3140957200974444958"
linkers = api.get_thread_likers(username, post_id=post_id)
print(linkers)
