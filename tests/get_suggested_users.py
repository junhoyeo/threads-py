import unittest
from threadspy import ThreadsAPI


class TestGetSuggestedUsers(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")

    def test_get_suggested_users(self):
        token = self.threads_api.get_token()
        self.assertIsInstance(token, str)
        self.assertEqual(token, self.threads_api.token)
        suggest = self.threads_api.get_suggested_users()
        self.assertIsInstance(suggest, list)


if __name__ == "__main__":
    unittest.main()
