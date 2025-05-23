import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

LOG_LEVEL = "DEBUG"  # DEBUG, INFO, WARNING, ERROR or "INFO" for production

# API settings
# Ensure GOOGLE_API_KEY is set in your environment variables or .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    # Use logger from main or raise an error early
    print("Error: GEMINI_API_KEY not found in environment variables")
    # In a production app, you might raise an exception or exit here.
    # For debugging, print and let the client creation potentially fail.

# Model settings
MODEL = "gemini-2.0-flash-live-001" # Or your chosen Live API model
VOICE_NAME = "Charon" # Or your preferred voice Puck, Charon, Kore, Fenrir, *Aoede*, Leda, Orus, and Zephyr.
LANGUAGE_CODE = "en-US" # Or your preferred language code
SYSTEM_INSTRUCTION = "You are a helpful voice assistant with camera and screen share view. Ensure every response clear and concise. Dont ask for additional information just make your best judgement." # Or your system instruction

# Server settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 9084))

# Session file path
SESSION_FILE = "session.json" # File to save the session handle

# Media handling
# MAX_CHUNK_SIZE = 4096  # 4KB