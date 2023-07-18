import unittest
from threadspy import ThreadsAPI
from time import sleep


class TestLikeAndUnLike(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
            # token="token"
        )

    def test_repost(self):
        post_id = self.threads_api.get_post_id_from_thread_id("CugF-EjhQ3r")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.repost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)

        post_id = self.threads_api.get_post_id_from_thread_id("Cuo1nCjNis1")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.repost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)

        post_id = self.threads_api.get_post_id_from_thread_id("CunBJvlBv2l")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.repost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)

    def test_unrepost(self):
        post_id = self.threads_api.get_post_id_from_thread_id("CugF-EjhQ3r")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.unrepost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)

        post_id = self.threads_api.get_post_id_from_thread_id("Cuo1nCjNis1")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.unrepost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)

        post_id = self.threads_api.get_post_id_from_thread_id("CunBJvlBv2l")  # or use `get_post_id_from_url`
        check_sum = self.threads_api.unrepost_thread(post_id=post_id)
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
