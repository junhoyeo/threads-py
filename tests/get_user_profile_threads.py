import unittest
from threadspy import ThreadsAPI


class TestGetUserProfileThreads(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.username = "_junhoyeo"
        self.user_id = "5438123050"

    def test_getUserProfileThreads(self):
        posts = self.threads_api.get_user_profile_threads(
            username=self.username, user_id=self.user_id
        )

        self.assertIsInstance(posts, list)
        self.assertIn("thread_items", posts[0].to_dict().keys())
        self.assertIsInstance(posts[0].thread_items, list)
        self.assertIn("post", posts[0].thread_items[0].to_dict().keys())


if __name__ == "__main__":
    unittest.main()
