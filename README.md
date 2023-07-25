# [<img src="./.github/logo.jpg" width="36" height="36" />](https://github.com/junhoyeo) threads-py

[![pypi](https://img.shields.io/pypi/v/threads-py.svg?style=flat-square&labelColor=black)](https://pypi.org/project/threads-py) [![MIT License](https://img.shields.io/badge/license-MIT-blue?style=flat-square&labelColor=black)](https://github.com/junhoyeo/threads-py/blob/main/LICENSE)


 ### **Unofficial, Reverse-Engineered Python API for [Meta's Threads](https://www.threads.net/).**

> #### **Looking for the TypeScript version?** _Check out **[junhoyeo/threads-api. ![](https://img.shields.io/github/stars/junhoyeo%2Fthreads-api?style=social)](https://github.com/junhoyeo/threads-api)**_

---

## Installation

```bash
pip install --no-cache-dir --upgrade threads-py
```

## Initialization
#### Public Data Usage:
```python3
from threadspy import ThreadsAPI
api = ThreadsAPI()
```
#### Private Data Usage:
```python3
from threadspy import ThreadsAPI
api = ThreadsAPI(
      username="Your-Username"
      password="Your-Password"
      token="You-Token" # optional (if you're already authenticated)
    )
```

---

## [<img src="./.github/emojis/pushpin.png" width="30" height="30" />](https://github.com/junhoyeo) Implementation Roadmap and Methodology Overview
- [x] 📢 [Read public data](#read-public-data)
  - [x] ✅ [Fetch User ID](#fetch-user-id)
  - [x] ✅ [Read User Profile Info](#read-user-profile-info)
  - [x] ✅ [Read list of User Threads](#read-list-of-user-threads)
    - [ ] 🚧 With Pagination (If auth provided)
  - [x] ✅ [Read list of User Replies](#read-list-of-user-replies)
    - [ ] 🚧 With Pagination (If auth provided)
  - [x] ✅ [Fetch Post ID](#fetch-post-id)
  - [x] ✅ [Read A Single Thread](#read-a-single-thread)
  - [x] ✅ [Get Thread Likes](#get-thread-likes)
- [x] 🔏 [Read user private data](#read-private-data)
  - [x] ✅ [Read User Followings](#read-user-followings)
  - [x] ✅ [Read User Followers](#read-user-followers)
  - [x] ✅ [Get suggested users](#get-suggested-users)
  - [x] ✅ [Search Query](#search-query)
  - [x] ✅ [Read User Timeline Feed](#read-user-timeline-feed)
- [ ] 🔏 [Write Private Data (Authentication Required)](#write-private-data-authentication-required)
  - [ ] ✅ (Create New Thrad Or Reply To Eexisting Thread)[#create-new-thrad-or-reply-to-eexisting-thread]
    - [ ] 🚧 Make link previews to get shown
  - [ ] ✅ [Delete Thread](#delete-thread)
  - [ ] 🚧 Quote Thread
- [x] 🔒 (Friendship Actions)[#friendship-actions-authentication-required]
  - [x] ✅ [Follow User](#follow-user)
  - [x] ✅ [Unfollow User](#unfollow-user)
  - [x] ✅ [Block User](#block-user)
  - [x] ✅ [Unblock User](#unblock-user)
  - [x] ✅ [Mute User](#mute-user)
  - [x] ✅ [Unmute User](#unmute-user)
  - [x] ✅ [Restrict User](#restrict-user)
  - [x] ✅ [Unrestrict User](#unrestrict-user)
  - [x] ✅ [Check Friendship Status With Another Users](#check-friendship-status-with-another-users)
- [x] 🔒 [Interactions (Authentication Required)](#interactions-authentication-required)
  - [x] ✅ [Like Thread](#like-thread)
  - [x] ✅ [Remove Like From Thread](#remove-like-from-thread)
  - [x] ✅ [Repost Thread](#repost-thread)
  - [x] ✅ [Delete Reposted Thread](#delete-reposted-thread)
- [ ] 🚧 LangChain Agent (`threadspy.ai`)
  - [ ] 🚧 Threads Tool for LangChain
  - [ ] 📌 Link Threads & LLaMa ([@Mineru98](https://github.com/Mineru98))
  - [ ] 📌 Provide statistical analysis of posts in Threads ([@Mineru98](https://github.com/Mineru98))



---
## Read public data



### Fetch User ID:

```python3
user_id = api.get_user_id_from_username(username)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
| `username` | Target username | String  |   Yes    |
</details>

### Read User Profile Info:

```python3
user_profile = api.get_user_profile(username, user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required | Default Value |
|:----------:|:---------------:|:-------:|:--------:|:-------------:|
| `username` | Target username | String  |   Yes    |       -       |
| `user_id`  | Target User ID  | String  |   No     |      None     |
</details> 



### Read list of User Threads:

```python3
user_threads = api.get_user_profile_threads(username, user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required | Default Value |
|:----------:|:---------------:|:-------:|:--------:|:-------------:|
| `username` | Target username | String  |   Yes    |       -       |
| `user_id`  | Target User ID  | String  |   No     |      None     |
</details>



### Read list of User Replies:

```python3
user_replies = api.get_user_profile_replies(username, user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required | Default Value |
|:----------:|:---------------:|:-------:|:--------:|:-------------:|
| `username` | Target username | String  |   Yes    |       -       |
| `user_id`  | Target User ID  | String  |   No     |      None     |
</details>



### Fetch Post ID:

> #### via Thread ID E.g. "CuW6-7KyXme":
```python3
post_id = api.get_post_id_from_thread_id(thread_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
| `thread_id`| Last part of the thread URL | String  |   Yes    |  
</details>
<details>
<summary>
<h4>Examples</h4>
</summary>

```
thread_id = 'CugF-EjhQ3r'
post_id = api.get_post_id_from_thread_id(thread_id)
```

</details>


#### via Post URL E.g."https://www.threads.net/t/CuW6-7KyXme":
```python3
post_id = api.get_post_id_from_url(post_url)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
| `post_url` |    Thread URL   | String  |   Yes    |
</details>
<details>
<summary>
<h4>Examples</h4>
</summary>

```
post_url = 'https://www.threads.net/t/CugF-EjhQ3r'
post_id = api.get_post_id_from_url(post_url)
```

</details>



### Read A Single Thread:

```python3
single_thread = api.get_threads(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
| `post_id`  | Target username | String  |   Yes    |
</details>



### Get Thread Likes:

```python3
thread_likes = api.get_thread_likers(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |    Description  |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
| `post_id`  | Target username | String  |   Yes    |
</details>






---
## Read Private Data 



### Read User Followings:

```python3
user_followers = api.get_followings(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` | Target User ID  | String  |   Yes    |
</details>



### Read User Followers:

```python3
user_followings = api.get_followers(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` | Target User ID  | String  |   Yes    |
</details>



### Get Suggested Users:

```python3
suggested_users = api.get_suggested_users(count, paging)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required | Default Value |
|:----------:|:---------------:|:-------:|:--------:|:-------------:|
|   `count`  | Number of suggested users  | Integer |    No    |      15       |
|  `paging`  | Page number  | Integer |    No    |      None     |
</details>



### Search Query:

```python3
thread_likes = api.search(search_parameter)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

|     Parameters     |    Description  |  Type   | Required |
|:------------------:|:---------------:|:-------:|:--------:|
| `search_parameter` |   Search Query  |  String |   Yes    |
</details>



### Read User Timeline Feed:

```python3
user_timeline = api.get_timeline(max_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

|Parameters|       Description      |  Type   | Required |
|:--------:|:----------------------:|:-------:|:--------:|
| `max_id` |   Next Posts Batch ID  |  String |    No    |
</details>







---
## Write Private Data (Authentication Required)



### Create New Thrad Or Reply To Eexisting Thread:

```python3
boolean_response = api.publish(count, image_path, url, parent_post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required | Default Value |
|:----------:|:---------------:|:-------:|:--------:|:-------------:|
|   `caption`  | Text to post in Thread | String |  Yes |    15    |
|  `image_path`  |   Image Path to post in Thread   | String |    No    |      None     |
|  `url`  |   Link to post in Thread   | String |    No    |      None     |
|  `parent_post_id`  |   Post ID   | String |    No    |      None     |
</details>
<details>
<summary>
<h4>Examples</h4>
</summary>

- Text Threads:

```python3
api.publish(caption="🤖 Hello World!")
```

- Threads with Image:

```python3
api.publish(
  caption= '🤖 Threads with Link Image',
  image_path="https://github.com/junhoyeo/threads-py/raw/main/.github/logo.jpg"
  )
```

- Threads with Link Attachment:

```python3
api.publish(
  caption= '🤖 Threads with Link Image',
  url="https://github.com/junhoyeo/threads-py"
  )
```

Reply to Other Threads:

```python3
parent_post_url = 'https://www.threads.net/t/CugF-EjhQ3r'
parent_post_id = api.get_post_id_from_url(parent_post_url) # or use `get_post_id_from_thread_id`

api.publish({
  text: '🤖 Beep',
  link: 'https://github.com/junhoyeo/threads-py',
  parent_post_id: parent_post_id,
})
```

</details>



### Delete Thread:

```python3
boolean_response = api.delete_thread(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `post_id` | Post Identifier | String  |    Yes   |
</details>







---
## Friendship Actions (Authentication Required)



### Follow User:

```python3
boolean_response = api.follow(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Unfollow User:

```python3
boolean_response = api.unfollow(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Block User:

```python3
boolean_response = api.block(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Unblock User:

```python3
boolean_response = api.unblock(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` | User Identifier  | String  |   Yes    |
</details>



### Mute User:

```python3
boolean_response = api.mute(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Unmute User:

```python3
boolean_response = api.unmute(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Restrict User:

```python3
boolean_response = api.restrict(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Unrestrict User:

```python3
boolean_response = api.unrestrict(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>



### Check Friendship Status With Another Users:

```python3
friendship_status = api.friendship_status(user_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `user_id` |  User Identifier  | String  |   Yes    |
</details>




---
## Interactions (Authentication Required)



### Like Thread:

```python3
boolean_response = api.like(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `post_id` |     Post Identifier     | String  |   Yes    |
</details>



### Remove Like From Thread:

```python3
boolean_response = api.unlike(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `post_id` |     Post Identifier     | String  |   Yes    |
</details>



### Repost Thread:

```python3
boolean_response = api.repost_thread(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `post_id` |     Post Identifier     | String  |   Yes    |
</details>


### Delete Reposted Thread:

```python3
boolean_response = api.unrepost_thread(post_id)
```
<details>
<summary>
<h4>Parameters</h4>
</summary>

| Parameters |   Description   |  Type   | Required |
|:----------:|:---------------:|:-------:|:--------:|
|  `post_id` |     Post Identifier     | String  |   Yes    |
</details>


</details>

---
## Contributors

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/junhoyeo">
          <img src="https://avatars.githubusercontent.com/u/32605822?v=4?s=100" width="100px;" alt="Junho Yeo"/>
          <br />
          <sub><b>Junho Yeo</b></sub>
        </a>
        <br />
        <a href="https://github.com/junhoyeo/threads-py/commits?author=junhoyeo" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Mineru98">
          <img src="https://avatars.githubusercontent.com/u/15326932?v=4?s=100" width="100px;" alt="iamiks"/>
          <br />
          <sub><b>iamiks</b></sub>
        </a>
        <br />
        <a href="https://github.com/junhoyeo/threads-py/commits?author=Mineru98" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/drunkleen">
          <img src="https://avatars.githubusercontent.com/u/26145653?v=4?s=100" width="100px;" alt="DrunkLeen"/>
          <br />
          <sub><b>DrunkLeen</b></sub>
        </a>
        <br />
        <a href="https://github.com/junhoyeo/threads-py/commits?author=drunkleen" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/ashrftvm">
          <img src="https://avatars.githubusercontent.com/u/16478713?v=4?s=100" width="100px;" alt="Asharaf Ali"/>
          <br />
          <sub><b>Asharaf Ali</b></sub>
        </a>
        <br />
        <a href="https://github.com/junhoyeo/threads-py/commits?author=ashrftvm" title="Code">💻</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/mirageoasis">
          <img src="https://avatars.githubusercontent.com/u/37329424?v=4?s=100" width="100px;" alt="mirageoasis"/>
          <br />
          <sub><b>mirageoasis</b></sub>
        </a>
        <br />
        <a href="https://github.com/junhoyeo/threads-py/commits?author=mirageoasis " title="Code">💻</a>
      </td>
    </tr>
  </tbody>
</table>


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
