import unittest
from threadspy import ThreadsAPI
from time import sleep


class TestGetNotifications(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(
            verbose=True,
            username="username",
            password="password",
            # token="token"
        )

    def test_get_notifications_replies(self):
        notifications = self.threads_api.get_notifications()
        self.assertIsInstance(notifications, dict)

    def test_get_notifications_mentions(self):
        notifications = self.threads_api.get_notifications(notification_filter='mentions')
        self.assertIsInstance(notifications, dict)

    def test_get_notifications_verified(self):
        notifications = self.threads_api.get_notifications(notification_filter='verified')
        self.assertIsInstance(notifications, dict)


if __name__ == "__main__":
    unittest.main()
