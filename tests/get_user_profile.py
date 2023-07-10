import unittest
from threadspy import ThreadsAPI


class TestGetUserProfile(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.username = "_junhoyeo"
        self.user_id = "5438123050"

    def test_get_user_profile(self):
        user = self.threads_api.get_user_profile(username=self.username, user_id=self.user_id)
        self.assertEqual(user.username, self.username)


if __name__ == "__main__":
    unittest.main()
