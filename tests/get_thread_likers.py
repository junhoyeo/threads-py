import unittest
from threadspy import ThreadsAPI


class TestGetThreadLikers(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.post_id = "3141675920411513399"

    def test_get_thread_likers(self):
        likers = self.threads_api.get_thread_likers(self.post_id)

        self.assertIsInstance(likers.users, list)
        self.assertIn("pk", likers.users[0].to_dict().keys())
        self.assertIn("full_name", likers.users[0].to_dict().keys())


if __name__ == "__main__":
    unittest.main()
