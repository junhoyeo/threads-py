import unittest
from threadspy import ThreadsAPI


class TestGetThreads(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True)
        self.post_id = "3140957200974444958"  # https://www.threads.net/t/CuW6-7KyXme

    def test_getThreads(self):
        thread = self.threads_api.get_threads(self.post_id)

        self.assertIn("reply_threads", thread.to_dict().keys())
        self.assertIn("containing_thread", thread.to_dict().keys())
        self.assertEqual(thread.containing_thread.id, self.post_id)
        self.assertIsInstance(thread.reply_threads, list)

        containing_thread_captions = [
            item.post.caption.text for item in thread.containing_thread.thread_items
        ]
        self.assertCountEqual(
            containing_thread_captions,
            [
                "This is fast. Could be made into a Mastodon API bridge like Skybridge (for Bluesky)",
                "For context, this is Skybridge https://skybridge.fly.dev/",
            ],
        )

        reply_thread_captions = [
            item.post.caption.text
            for reply_thread in thread.reply_threads
            for item in reply_thread.thread_items
        ]
        self.assertEqual(reply_thread_captions[0], "🤍💙🤍💙💙")


if __name__ == "__main__":
    unittest.main()
