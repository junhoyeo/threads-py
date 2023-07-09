import unittest
from threadspy import ThreadsAPI


class TestGetToken(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")

    def test_get_token(self):
        check_sum = self.threads_api.get_token()
        self.assertIsInstance(check_sum, bool)
        self.assertIsInstance(self.threads_api.token, str)


if __name__ == "__main__":
    unittest.main()
