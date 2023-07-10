import unittest
from threadspy import ThreadsAPI


class TestLikeAndUnLike(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
        )
        self.post_id = "3140957200974444958"

    def test_like(self):
        check_sum = self.threads_api.like(post_id=self.post_id)
        self.assertEqual(check_sum, True)

    def test_unlike(self):
        check_sum = self.threads_api.unlike(post_id=self.post_id)
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
