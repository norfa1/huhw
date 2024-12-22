import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_api_key() -> str:
    """Returns the Google API key."""
    # WARNING: Do not commit this API key to version control!
    return os.getenv("GOOGLE_API_KEY")