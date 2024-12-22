import json
from typing import Dict, Any
import os
from core_functions import (
    save_memory,
    retrieve_memory_from_file,
    update_memory,
)
from prompt_utils import build_prompt, generate_response

MEMORY_FILE = "chatbot_memory.json"

def process_request(memory: Dict[str, Any]) -> None:
    """Processes user requests and generates responses."""
    try:
        while True:
          print("DEBUG: Waiting for user input...")  # Debugging message
          user_input = input("You: ")
          print(f"DEBUG: User input: {user_input}") # Debugging message
          if user_input.lower() == "exit":
              break

          # Placeholder for intent and entity extraction (you will expand here later)
          intent = "unknown"
          entities = {}

          updated_memory = update_memory(
              memory,
              user_input,
              "Bot: Response pending...",
              intent,
              entities,
          )
          prompt = build_prompt(user_input, updated_memory["context"])
          response = generate_response(prompt)

          if response:
            updated_memory = update_memory(
                updated_memory,
                user_input,
                f"Bot: {response}",
                intent,
                entities,
            )
            print(f"Bot: {response}")
          else:
              print("Bot: Error generating response.")
          save_memory(updated_memory, MEMORY_FILE)
          memory = updated_memory
    except EOFError:
        print("DEBUG: EOF detected. Saving memory.") # Debugging message
        save_memory(memory, MEMORY_FILE)
    except Exception as e:
        print(f"DEBUG: An unexpected error occurred: {e}") # Debugging message
        save_memory(memory, MEMORY_FILE)

def main() -> None:
    """Main function to start the chatbot."""
    memory_file = os.path.join("brain_memory", MEMORY_FILE)
    memory = retrieve_memory_from_file(memory_file)
    if not memory:
        memory = {
            'user_history': [],
            'bot_history': [],
            'context': {
                'intent': '',
                'entities': {}
            }
        }
    process_request(memory)

if __name__ == "__main__":
    main()