import unittest
from threadspy import ThreadsAPI


class TestLikeAndUnLike(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
        )

    def test_like(self):
        post_url = "https://www.threads.net/t/CugF-EjhQ3r"
        post_id = self.threads_api.get_post_id_from_url(
            post_url
        )  # or use `get_post_id_from_thread_id`
        check_sum = self.threads_api.like(post_id=post_id)
        self.assertEqual(check_sum, True)

    def test_unlike(self):
        post_url = "https://www.threads.net/t/CugF-EjhQ3r"
        post_id = self.threads_api.get_post_id_from_url(
            post_url
        )  # or use `get_post_id_from_thread_id`
        check_sum = self.threads_api.unlike(post_id=post_id)
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
