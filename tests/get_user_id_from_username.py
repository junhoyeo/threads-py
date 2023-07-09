import unittest
from threadspy import ThreadsAPI


class TestGetUserIdFromUsername(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.username = "_junhoyeo"

    def test_fetching_postID_with_threadID(self):
        user_id = self.threads_api.get_user_id_from_username(self.username)
        self.assertIsInstance(user_id, str)
        self.assertEqual(user_id, self.threads_api.user_id)
        self.assertEqual(user_id, "5438123050")


if __name__ == "__main__":
    unittest.main()
