import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_USERNAME=os.environ.get("POSTGRES_USERNAME")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_SERVER=os.environ.get("POSTGRES_SERVER")
POSTGRES_SCHEMA=os.environ.get("POSTGRES_SCHEMA")
