import unittest
from threadspy import ThreadsAPI


class TestGetToken(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")

    def test_get_token(self):
        token = self.threads_api.get_token()
        self.assertIsInstance(token, str)
        self.assertEqual(token, self.threads_api.token)


if __name__ == "__main__":
    unittest.main()
