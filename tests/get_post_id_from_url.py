import unittest
from threadspy import ThreadsAPI


class TestGetPostIDfromURL(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.post_url = "https://www.threads.net/t/CuX_UYABrr7/?igshid=MzRlODBiNWFlZA=="
        self.post_id = None

    def test_fetching_postID_with_postURL(self):
        self.post_id = self.threads_api.get_post_id_from_url(self.post_url)
        self.assertEqual(self.post_id, "3141257742204189435")


if __name__ == "__main__":
    unittest.main()
