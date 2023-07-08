import unittest
from threadspy import ThreadsAPI


class TestGetPostIDfromThreadID(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.thread_id = "CuX_UYABrr7"
        self.post_id = None

    def test_fetching_postID_with_threadID(self):
        self.post_id = self.threads_api.get_post_id_from_thread_id(self.thread_id)
        self.assertEqual(self.post_id, "3141257742204189435")


if __name__ == "__main__":
    unittest.main()
