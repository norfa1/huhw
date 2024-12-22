import json
from typing import Dict, Any, Union


def save_memory(memory: Dict, filename: str) -> None:
    """
    Saves the memory data to a JSON file.

    Args:
        memory: The memory dictionary to be saved.
        filename: The name of the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(memory, f, indent=2)


def retrieve_memory_from_file(filename: str) -> Dict:
    """
    Retrieves the memory data from a JSON file.

    Args:
        filename: The name of the JSON file.

    Returns:
        The loaded memory dictionary.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist


def store_memory(memory: Dict[str, Any], key: str, content: Dict[str, Any]) -> Dict[str, Any]:
    """
    Stores new content into memory with the given key.

    Args:
        memory: The current memory dictionary.
        key: The key to store the content under.
        content: The content to be stored (as a dictionary).

    Returns:
        The updated memory dictionary.
    """
    updated_memory = memory.copy()  # Create a copy to ensure immutability
    updated_memory[key] = content
    return updated_memory


def retrieve_memory(memory: Dict[str, Any], key: str) -> Union[Dict[str, Any], None]:
    """
    Retrieves memory content by key.

    Args:
        memory: The current memory dictionary.
        key: The key to retrieve.

    Returns:
        The content associated with the key, or None if the key doesn't exist.
    """
    return memory.get(key)


def update_memory(memory: Dict[str, Any], user_input: str, response: str, intent: str, entities: Dict[str, str]) -> Dict[str, Any]:
    """
    Updates the memory with conversation history.

    Args:
        memory: The current memory dictionary.
        user_input: The user's input.
        response: The chatbot's response.
        intent: The identified intent of the user's input.
        entities: Extracted entities from the user's input.

    Returns:
        The updated memory dictionary.
    """
    updated_memory = memory.copy()  # Create a copy to ensure immutability
    updated_memory['user_history'].append(user_input)
    updated_memory['bot_history'].append(response)
    updated_memory['context']['intent'] = intent
    updated_memory['context']['entities'] = entities
    return updated_memory


def search_knowledge_base(knowledge_base: Dict, search_key: str, search_value: str) -> Union[str, None]:
    """
    Searches for a specific entry in the knowledge base.

    Args:
        knowledge_base: The knowledge base dictionary.
        search_key: The key to search for.
        search_value: The value to search for.

    Returns:
        The value associated with the search_key if found, otherwise None.
    """
    for key, value in knowledge_base.items():
        if key.lower() == search_key.lower(): 
            return value
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.lower() == search_value.lower():
                    return value
    return None