import unittest
from threadspy import ThreadsAPI


class TestFollowingAndUnFollowing(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
        )
        self.username = "zuck"

    def test_follow(self):
        target_user_id = self.threads_api.get_user_id_from_username(self.username)
        check_sum = self.threads_api.follow(user_id=target_user_id)
        self.assertEqual(check_sum, True)

    def test_unfollow(self):
        target_user_id = self.threads_api.get_user_id_from_username(self.username)
        check_sum = self.threads_api.unfollow(user_id=target_user_id)
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()
