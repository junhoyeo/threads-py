import unittest
from threadspy import ThreadsAPI


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")
        self.thread_id = "CuX_UYABrr7"
        self.post_id = None

    def test_publish(self):
        checkSum = self.threads_api.publish("Hello World!")
        self.assertEqual(checkSum, True)


if __name__ == "__main__":
    unittest.main()
