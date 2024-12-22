import unittest
from prompt_utils import build_prompt
from unittest.mock import patch, MagicMock
from prompt_utils import generate_response
from config import get_api_key
import google.generativeai as genai


class TestBuildPrompt(unittest.TestCase):

    def test_build_prompt_with_empty_context(self):
        user_input = "Hello, how are you?"
        context = {}
        expected_prompt = """
    You are a helpful assistant.
    User Input: Hello, how are you?
    Current Intent: unknown
    Current Entities: {}
    Answer the user input based on the provided context
    """
        actual_prompt = build_prompt(user_input, context)
        self.assertEqual(actual_prompt.strip(), expected_prompt.strip())

    def test_build_prompt_with_context(self):
        user_input = "What is the weather in London?"
        context = {
            "intent": "weather_inquiry",
            "entities": {"location": "London"}
        }
        expected_prompt = """
    You are a helpful assistant.
    User Input: What is the weather in London?
    Current Intent: weather_inquiry
    Current Entities: {'location': 'London'}
    Answer the user input based on the provided context
    """
        actual_prompt = build_prompt(user_input, context)
        self.assertEqual(actual_prompt.strip(), expected_prompt.strip())

    def test_build_prompt_with_missing_entities(self):
        user_input = "Tell me a joke"
        context = {
            "intent": "joke_request",
        }
        expected_prompt = """
    You are a helpful assistant.
    User Input: Tell me a joke
    Current Intent: joke_request
    Current Entities: {}
    Answer the user input based on the provided context
    """
        actual_prompt = build_prompt(user_input, context)
        self.assertEqual(actual_prompt.strip(), expected_prompt.strip())


class TestGenerateResponse(unittest.TestCase):

    @patch('prompt_utils.genai.GenerativeModel')
    def test_generate_response_success(self, mock_generative_model):
        mock_response = MagicMock()
        mock_response.text = "This is a test response from the LLM."
        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        mock_generative_model.return_value = mock_model
        prompt = "Test prompt"
        response = generate_response(prompt)
        self.assertEqual(response, "This is a test response from the LLM.")

    @patch('prompt_utils.genai.GenerativeModel')
    def test_generate_response_error(self, mock_generative_model):
        mock_generative_model.side_effect = Exception("API Error")
        prompt = "Test prompt"
        response = generate_response(prompt)
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()