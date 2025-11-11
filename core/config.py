import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")
DATABASE_NAME = "buckminster_db"