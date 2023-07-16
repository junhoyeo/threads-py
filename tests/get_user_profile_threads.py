import unittest
from threadspy import ThreadsAPI


class TestGetUserProfileThreads(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.username = "_junhoyeo"

    def test_get_user_profile_threads(self):
        user_id = self.threads_api.get_user_id_from_username(username=self.username)
        posts = self.threads_api.get_user_profile_threads(
            username=self.username, user_id=user_id
        )

        self.assertIsInstance(posts, list)
        if len(posts) > 0:
            self.assertIn("thread_items", posts[0].to_dict().keys())
            self.assertIsInstance(posts[0].thread_items, list)
            self.assertIn("post", posts[0].thread_items[0].to_dict().keys())


if __name__ == "__main__":
    unittest.main()
