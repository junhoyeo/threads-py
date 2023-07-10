import unittest
from threadspy import ThreadsAPI


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
        )

    def test_publish(self):
        check_sum = self.threads_api.publish("🤖 Hello World!")
        self.assertEqual(check_sum, True)

    def test_publish_with_attach_link(self):
        check_sum = self.threads_api.publish(
            "🤖 Hello World!", url="https://github.com/junhoyeo/threads-py)"
        )
        self.assertEqual(check_sum, True)

    def test_publish_with_reply(self):
        parent_post_url = "https://www.threads.net/t/CugF-EjhQ3r"
        parent_post_id = self.threads_api.get_post_id_from_url(parent_post_url)
        check_sum = self.threads_api.publish("🤖 Hello World!", parent_post_id=parent_post_id)
        self.assertEqual(check_sum, True)

    def test_publish_with_image_url(self):
        image_path = "https://github.com/junhoyeo/threads-py/blob/main/.github/logo.jpg"
        check_sum = self.threads_api.publish("🤖 Hello World!", image_path=image_path)
        self.assertEqual(check_sum, True)

    def test_publish_with_local_image(self):
        check_sum = self.threads_api.publish("🤖 Hello World!", image_path=".github/logo.jpg")
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
