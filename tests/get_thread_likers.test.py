from threadspy import ThreadsAPI

api = ThreadsAPI()
username = "_junhoyeo"
post_id = "3140623946340547898"
linkers = api.get_thread_likers(username, post_id=post_id)
print(linkers)
