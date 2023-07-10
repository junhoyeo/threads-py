import unittest
from threadspy import ThreadsAPI


class TestGetUserProfileReplies(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.username = "_junhoyeo"
        self.user_id = "5438123050"

    def test_get_user_profile_replies(self):
        posts = self.threads_api.get_user_profile_replies(
            username=self.username, user_id=self.user_id
        )

        self.assertIsInstance(posts, list)
        self.assertIn("thread_items", posts[0].to_dict())
        self.assertGreaterEqual(len(posts[0].thread_items), 2)


if __name__ == "__main__":
    unittest.main()
