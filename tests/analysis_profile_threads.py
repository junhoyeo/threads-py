import unittest
from threadspy import ThreadsAgent


class TestAnalysisProfile(unittest.TestCase):
    def setUp(self):
        self.agent = ThreadsAgent(mode="openai", OPENAI_API_KEY="OPENAI_API_KEY")

    def test_analysis_profile(self):
        threads = self.agent.analysis_profile(
            username="zuck", boundary="threads", onlyText=True, sort="DESC"
        )
        threads = list(map(lambda x: x["text"], threads))
        self.assertIsInstance(threads, list)


if __name__ == "__main__":
    unittest.main()
