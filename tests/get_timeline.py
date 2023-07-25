import unittest
from threadspy import ThreadsAPI
from time import sleep


class TestGetTimeline(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
            # token="token"
        )

    def test_get_timeline_wo_max_id(self):
        timeline = self.threads_api.get_timeline()
        self.assertIsInstance(timeline, dict)

    def test_get_timeline_w_max_id(self):
        timeline = self.threads_api.get_timeline(max_id=2)
        self.assertIsInstance(timeline, dict)


if __name__ == "__main__":
    unittest.main()
