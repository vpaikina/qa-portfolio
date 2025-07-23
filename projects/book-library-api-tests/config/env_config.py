import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
EXTERNAL_API_URL = os.getenv(
    "EXTERNAL_API_URL", "https://fakerestapi.azurewebsites.net/api/v1"
)
