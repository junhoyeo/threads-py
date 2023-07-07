# [<img src="./assets/logo.jpg" width="36" height="36" />](https://github.com/junhoyeo) threads-py

> Unofficial, Reverse-Engineered Python client for Meta's Threads.

## Installation

```bash
pip install threadspy
```

## Usages

```python
from threadspy._thread import ThreadsAPI

api = ThreadsAPI()

username = "{username}"

user_id = api.get_user_id_from_username(username)
print(user_id)

profile = api.get_user_profile(username, user_id=user_id)
print(profile)

threads = api.get_user_profile_threads(username, user_id=user_id)
print(threads)

post_id = "{post_id}"
thread = api.get_user_profile_thread(username, post_id=post_id)
print(thread)

threads = api.get_user_profile_replies(username, user_id=user_id)
print(threads)

linkers = api.get_thread_likers(username, post_id=post_id)
print(linkers)
```

## License

<p align="center">
  <a href="https://github.com/junhoyeo">
    <img src="./assets/labtocat.png" width="256" height="256">
  </a>
</p>

<p align="center">
  <strong>MIT © <a href="https://github.com/junhoyeo">Junho Yeo</a></strong>
</p>

If you find this project intriguing, **please consider starring it(⭐)** or following me on [GitHub](https://github.com/junhoyeo) (I wouldn't say [Threads](https://www.threads.net/@_junhoyeo)).