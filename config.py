"""
Configuration for LLM Behavior Analyzer
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Model Configuration
DEFAULT_MODELS = {
    "claude": "claude-sonnet-4-20250514",
    "gpt": "gpt-4-turbo-preview"
}

# Analysis Configuration
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 1000
NUM_ITERATIONS = 5  # How many times to test each prompt variation

# Output Configuration
RESULTS_DIR = "results"
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"