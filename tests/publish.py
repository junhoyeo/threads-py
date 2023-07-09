import unittest
from threadspy import ThreadsAPI


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")

    def test_publish(self):
        check_sum = self.threads_api.publish("Hello World!")
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
