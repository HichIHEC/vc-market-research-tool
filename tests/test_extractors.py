Sure, here's the contents for the file `/vc-market-research-tool/vc-market-research-tool/tests/test_extractors.py`:

import unittest
from src.data.extractors import extract_data_from_serper, refine_query

class TestExtractors(unittest.TestCase):

    def test_extract_data_from_serper(self):
        query = "latest trends in AI startups"
        response = extract_data_from_serper(query)
        self.assertIsInstance(response, dict)
        self.assertIn('results', response)
        self.assertGreater(len(response['results']), 0)

    def test_refine_query(self):
        initial_query = "AI startups"
        refined_query = refine_query(initial_query)
        self.assertNotEqual(initial_query, refined_query)
        self.assertIn("AI", refined_query)

if __name__ == '__main__':
    unittest.main()