#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv, find_dotenv


if __name__ == "__main__":
    if (find_dotenv() != ""):
        print("\nWARNING! Missing configuration.\nThere is no .env file to get the enviroment variables\nMake a .env file and add the following:")
        print("MATRIX_MODE='example'")
        print("DATABASE_URL='localhost:8080'")
        print("API_KEY='12345abcdef'")
        print("LOG_LEVEL='USER'")
        print("ZION_ENDPOINT='https://example.com'")
    else:
        load_dotenv()
        print(f"MATRIX_MODE='{os.getenv('MATRIX_MODE')}'")
        print(f"DATABASE_URL='{os.getenv('DATABASE_URL')}'")
        print(f"API_KEY='{os.getenv('API_KEY')}'")
        print(f"LOG_LEVEL='{os.getenv('LOG_LEVEL')}'")
        print(f"ZION_ENDPOINT='{os.getenv('ZION_ENDPOINT')}'")
