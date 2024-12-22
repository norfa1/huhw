import google.generativeai as genai
from typing import Optional, Dict, Any
from config import get_api_key


def generate_response(prompt: str) -> Optional[str]:
    """
    Generates a response from the LLM API.

    Args:
        prompt: The prompt to send to the LLM.

    Returns:
        The response from the LLM, or None if an error occurs.
    """
    try:
        api_key = get_api_key()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None


def build_prompt(user_input: str, context: Dict[str, Any]) -> str:
    """
    Constructs a prompt for the LLM, with more specific context.

    Args:
        user_input: The user's input.
        context: The current context of the conversation.

    Returns:
        A formatted prompt string.
    """
    intent = context.get("intent", "unknown")
    entities = context.get("entities", {})
    prompt = f"""
    You are a helpful assistant.
    User Input: {user_input}
    Current Intent: {intent}
    Current Entities: {entities}
    Answer the user input based on the provided context
    """
    return prompt