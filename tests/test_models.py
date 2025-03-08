Sure, here's the contents for the file `/vc-market-research-tool/vc-market-research-tool/tests/test_models.py`:

import unittest
from src.models.llm import LLM
from src.models.embeddings import generate_embeddings

class TestLLM(unittest.TestCase):
    def setUp(self):
        self.llm = LLM(model_name='Llama-3-8B')

    def test_load_model(self):
        self.assertIsNotNone(self.llm.load_model())

    def test_context_aware_extraction(self):
        input_text = "This is a test startup description."
        output = self.llm.context_aware_extraction(input_text)
        self.assertIsInstance(output, dict)

class TestEmbeddings(unittest.TestCase):
    def test_generate_embeddings(self):
        data = ["sample text 1", "sample text 2"]
        embeddings = generate_embeddings(data)
        self.assertEqual(len(embeddings), len(data))
        self.assertTrue(all(isinstance(embedding, list) for embedding in embeddings))

if __name__ == '__main__':
    unittest.main()