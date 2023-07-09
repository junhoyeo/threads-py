import unittest
from threadspy import ThreadsAgent


class TestAnalysisProfileReplies(unittest.TestCase):
    def setUp(self):
        self.agent = ThreadsAgent(mode="openai", OPENAI_API_KEY="OPENAI_API_KEY")

    def test_analysis_profile_replies(self):
        replies = self.agent.analysis_profile(
            username="zuck", boundary="replies", onlyText=True, sort="DESC"
        )
        replies = list(map(lambda x: x["text"], replies))
        print(replies)
        self.assertIsInstance(replies, list)


if __name__ == "__main__":
    unittest.main()
