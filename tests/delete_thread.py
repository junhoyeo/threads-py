import unittest
from threadspy import ThreadsAPI


class TestDeleteThread(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
            # token="token"
        )

    def test_delete_thread(self):
        post_id = self.threads_api.delete_thread(
            "CugF-EjhQ3r"
        )  # or use `get_post_id_from_url`
        check_sum = self.threads_api.repost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
