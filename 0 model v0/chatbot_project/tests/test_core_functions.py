import unittest
from core_functions import (
    save_memory, 
    retrieve_memory_from_file, 
    store_memory, 
    retrieve_memory, 
    update_memory, 
    search_knowledge_base
)

class TestCoreFunctions(unittest.TestCase):

    def test_save_memory_and_retrieve_memory_from_file(self):
        """
        Tests saving memory to a file and retrieving it back.
        """
        memory = {
            'user_history': ['Hello', 'How are you?'],
            'bot_history': ['Hi!', 'I am doing well, thank you.'],
            'context': {'intent': 'greeting'}
        }
        filename = 'test_memory.json'
        save_memory(memory, filename)
        loaded_memory = retrieve_memory_from_file(filename)
        self.assertEqual(memory, loaded_memory)

    def test_store_memory(self):
        """
        Tests storing new content in the memory.
        """
        memory = {'user_history': []}
        new_key = 'user_name'
        new_content = {'value': 'John Doe'}
        updated_memory = store_memory(memory, new_key, new_content)
        self.assertIn(new_key, updated_memory)
        self.assertEqual(updated_memory[new_key], new_content)

    def test_retrieve_memory(self):
        """
        Tests retrieving memory content by key.
        """
        memory = {'user_history': [], 'user_name': {'value': 'Alice'}}
        key = 'user_name'
        retrieved_content = retrieve_memory(memory, key)
        self.assertEqual(retrieved_content, {'value': 'Alice'})

    def test_update_memory(self):
        """
        Tests updating memory with conversation history.
        """
        memory = {
            'user_history': [],
            'bot_history': [],
            'context': {
                'intent': '',
                'entities': {}
            }
        }
        user_input = "What's the weather today?"
        response = "Let me check..."
        intent = "weather_check"
        entities = {'location': 'London'}
        updated_memory = update_memory(memory, user_input, response, intent, entities)
        self.assertEqual(updated_memory['user_history'], [user_input])
        self.assertEqual(updated_memory['bot_history'], [response])
        self.assertEqual(updated_memory['context']['intent'], intent)
        self.assertEqual(updated_memory['context']['entities'], entities)

    def test_search_knowledge_base(self):
        """
        Tests searching for entries in the knowledge base.
        """
        knowledge_base = {
            'colors': ['red', 'green', 'blue'],
            'fruits': ['apple', 'banana', 'orange'],
            'cities': ['London', 'Paris', 'New York']
        }
        self.assertEqual(search_knowledge_base(knowledge_base, 'colors', 'red'), ['red', 'green', 'blue'])
        self.assertEqual(search_knowledge_base(knowledge_base, 'fruits', 'apple'), ['apple', 'banana', 'orange'])
        self.assertEqual(search_knowledge_base(knowledge_base, 'cities', 'London'), ['London', 'Paris', 'New York'])
        self.assertIsNone(search_knowledge_base(knowledge_base, 'animals', 'dog')) 

if __name__ == '__main__':
    unittest.main()