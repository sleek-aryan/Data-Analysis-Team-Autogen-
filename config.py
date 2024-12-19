import os
import tempfile

temp_dir = tempfile.TemporaryDirectory()

config_list = [
    {
        "model": "gpt-4o-mini-2024-07-18",
        "api_key": "ENTER_YOUR_API_KEY"
    }
]

llm_config = {
    "temperature": 0,
    "config_list": config_list,
    "top_p": 0.3,
    "seed": 42,
}

DEFAULT_DATASET_PATH = "C:\\Users\\Aryan Gurav\\Desktop\\AGENTIC_CLEAN\\dataset"