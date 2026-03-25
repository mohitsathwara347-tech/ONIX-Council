import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

CHAIRMAN = {
    "name": os.getenv("CHAIRMAN_NAME"),
    "model": os.getenv("CHAIRMAN_MODEL"),
    "api_key": os.getenv("CHAIRMAN_API_KEY"),
}

MEMBERS = [
    {
        "name": os.getenv("MEMBER1_NAME"),
        "model": os.getenv("MEMBER1_MODEL"),
        "api_key": os.getenv("MEMBER1_API_KEY"),
    },
    {
        "name": os.getenv("MEMBER2_NAME"),
        "model": os.getenv("MEMBER2_MODEL"),
        "api_key": os.getenv("MEMBER2_API_KEY"),
    },
    {
        "name": os.getenv("MEMBER3_NAME"),
        "model": os.getenv("MEMBER3_MODEL"),
        "api_key": os.getenv("MEMBER3_API_KEY"),
    },
    {
        "name": os.getenv("MEMBER4_NAME"),
        "model": os.getenv("MEMBER4_MODEL"),
        "api_key": os.getenv("MEMBER4_API_KEY"),
    },
]
