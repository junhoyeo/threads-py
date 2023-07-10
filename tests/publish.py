import unittest
from threadspy import ThreadsAPI


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
            token="eyJkc191c2VyX2lkIjoiNTg0NTY2MDA5NDciLCJzZXNzaW9uaWQiOiI1ODQ1NjYwMDk0NyUzQWJaTm9NUEFOTVFYVGs3JTNBMTQlM0FBWWQ1c083WGg1Qy1RRjVHUWd6QWNOQWRDT2dzZl9zcXBIeVFNT0NPTncifQ==",
        )

    def test_publish(self):
        check_sum = self.threads_api.publish("🤖 Hello World!")
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
