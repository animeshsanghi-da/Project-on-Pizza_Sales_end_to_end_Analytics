# utils.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Load environment variables from .env file
load_dotenv()

def get_db_engine():
    """
    Creates and returns a SQLAlchemy Engine instance using environment variables.
    """
    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME")
    )
    
    return create_engine(connection_url)