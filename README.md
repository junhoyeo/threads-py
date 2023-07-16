# [<img src="./.github/logo.jpg" width="36" height="36" />](https://github.com/junhoyeo) threads-py

[![pypi](https://img.shields.io/pypi/v/threads-py.svg?style=flat-square&labelColor=black)](https://pypi.org/project/threads-py) [![MIT License](https://img.shields.io/badge/license-MIT-blue?style=flat-square&labelColor=black)](https://github.com/junhoyeo/threads-py/blob/main/LICENSE)

> Unofficial, Reverse-Engineered Python client for Meta's Threads.

**Looking for the TypeScript version?** _Check out **[junhoyeo/threads-api. ![](https://img.shields.io/github/stars/junhoyeo%2Fthreads-api?style=social)](https://github.com/junhoyeo/threads-api)**_

## Installation

```bash
pip install --no-cache-dir --upgrade threads-py
```

<details>
<summary><h3>🚀 Usage (Read)</h3></summary>

```python
from threadspy import ThreadsAPI

api = ThreadsAPI()

username = "{username}"

# get a user id
user_id = api.get_user_id_from_username(username)
print(user_id)

# get a profile info
profile = api.get_user_profile(username, user_id=user_id)
print(profile)

# get a profile's threads tab
threads = api.get_user_profile_threads(username, user_id=user_id)
print(threads)

# get a profile's replies tab
replies = api.get_user_profile_replies(username, user_id=user_id)
print(replies)

# 3-ways to get the {post_id}
thread_id = "CuX_UYABrr7"
post_id = api.get_post_id_from_thread_id(thread_id)
print(post_id)

post_url = "https://www.threads.net/t/CuX_UYABrr7/?igshid=MzRlODBiNWFlZA=="
post_id = api.get_post_id_from_url(post_url)
print(post_id)

thread_id = "CuX_UYABrr7"
post_id = api.get_post_id_from_thread_id(thread_id)
print(post_id)

# get threads info
thread = api.get_threads(post_id)
print(thread)

# get who liked a thread
linkers = api.get_thread_likers(post_id)
print(linkers)
```
</details>

### 🚀 Usage (Write)

#### ✨ Text Threads

```python
from threadspy import ThreadsAPI

api = ThreadsAPI(username="username", password="password")
api.publish(caption="🤖 Hello World!")
```

#### ✨ Threads with Image

```python
api.publish(caption= '🤖 Threads with Link Image', image_path="https://github.com/junhoyeo/threads-py/raw/main/.github/logo.jpg")
```

#### ✨ Threads with Link Attachment

```python
api.publish(caption= '🤖 Threads with Link Attachment', url="https://github.com/junhoyeo/threads-py)")
```

#### ✨ Reply to Other Threads

```python
parent_post_url = 'https://www.threads.net/t/CugF-EjhQ3r'
parent_post_id = api.get_post_id_from_url(parent_post_url) # or use `get_post_id_from_thread_id`

api.publish({
  text: '🤖 Beep',
  link: 'https://github.com/junhoyeo/threads-py',
  parent_post_id: parent_post_id,
})
```

#### 🔎 Search Users

```python
search_parameter = "DrunkLeen"
# 💡 Uses current credentials
api.search(search_parameter)
```

#### 👍 Like/Unlike a Thread

```python
post_url = 'https://www.threads.net/t/CugF-EjhQ3r'
post_id = api.get_post_id_from_url(post_url) # or use `get_post_id_from_thread_id`

# 💡 Uses current credentials
api.like(postIDToLike)
api.unlike(postIDToLike)
```

#### 👉 Follow/Unfollow a User

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.follow(user_id)
api.unfollow(user_id)
```

#### ⛔ Block/Unblock a User

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.block(user_id)
api.unblock(user_id)
```

#### 🔇 Mute/Unmute a User

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.mute(user_id)
api.unmute(user_id)
```

#### ⏹️ Restrict/Unrestrict a User

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.restrict(user_id)
api.unrestrict(user_id)
```

#### 🧑‍🦳 Check FriendshipStatus with a User

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.friendship_status(user_id)
```

#### 🧑‍🦳 Get User Followings and Followers

```python
user_id = api.get_user_id_from_username('junhoyeo')

# 💡 Uses current credentials
api.get_followings(user_id)
api.get_followers(user_id)
```


## [<img src="./.github/emojis/pushpin.png" width="30" height="30" />](https://github.com/junhoyeo) Roadmap

- [x] ✅ Read public data
  - [x] ✅ Fetch UserID(`314216`) via username(`zuck`)
  - [ ] 🚧 Read timeline feed
  - [x] ✅ Read User Profile Info
  - [x] ✅ Read list of User Threads
    - [ ] 🚧 With Pagination (If auth provided)
  - [x] ✅ Read list of User Replies
    - [ ] 🚧 With Pagination (If auth provided)
  - [x] ✅ Fetch PostID(`3140957200974444958`) via ThreadID(`CuW6-7KyXme`) or PostURL(`https://www.threads.net/t/CuW6-7KyXme`)
  - [x] ✅ Read Threads via PostID
  - [x] ✅ Read Likers in Thread via PostID
- [ ] 🚧 LangChain Agent (`threadspy.ai`)
  - [ ] 🚧 Threads Tool for LangChain
  - [ ] 📌 Link Threads & LLaMa ([@Mineru98](https://github.com/Mineru98))
  - [ ] 📌 Provide statistical analysis of posts in Threads ([@Mineru98](https://github.com/Mineru98))
- [x] ✅ Read user private data
  - [x] ✅ Read User Followers
  - [x] ✅ Read User Followings
- [ ] 🚧 Write data (i.e. write automated Threads)
  - [ ] 🚧 Create new Thread with text
    - [ ] 🚧 Make link previews to get shown
  - [ ] 🚧 Create new Thread with media
  - [ ] 🚧 Create new Thread with multiple images
  - [ ] 🚧 Reply to existing Thread
  - [ ] 🚧 Quote Thread
  - [ ] 🚧 Delete Thread
- [x] ✅ Friendships
  - [x] ✅ Follow User
  - [x] ✅ Unfollow User
  - [x] ✅ Block User
  - [x] ✅ Unblock User
  - [x] ✅ Mute User
  - [x] ✅ Unmute User
  - [x] ✅ Restrict User
  - [x] ✅ Unrestrict User
  - [x] ✅ Check FriendshipStatus with a User
- [x] ✅ Interactions
  - [x] ✅ Like Thread
  - [x] ✅ Unlike Thread

## License

<p align="center">
  <a href="https://github.com/junhoyeo">
    <img src="./.github/labtocat.png" width="256" height="256">
  </a>
</p>

<p align="center">
  <strong>MIT © <a href="https://github.com/junhoyeo">Junho Yeo</a></strong>
</p>

If you find this project intriguing, **please consider starring it(⭐)** or following me on [GitHub](https://github.com/junhoyeo) (I wouldn't say [Threads](https://www.threads.net/@_junhoyeo)).
