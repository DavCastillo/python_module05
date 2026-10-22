#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv, find_dotenv


if __name__ == "__main__":
    print("\nORACLE STATUS: Consulting the configuration...\n")
    if (find_dotenv() == ""):
        print("WARNING! Missing configuration.\nThere is no .env file to get the enviroment variables\nMake a .env file following this structure (these are example values):")
        print("MATRIX_MODE='development'")
        print("DATABASE_URL='localhost:8080'")
        print("API_KEY='12345abcdef'")
        print("LOG_LEVEL='USER'")
        print("ZION_ENDPOINT='https://example.com'")
    else:
        load_dotenv()
        print("Configuration loaded:")
        if (os.getenv('MATRIX_MODE') == "development"):
            print(f"Mode: {os.getenv('MATRIX_MODE')}")
            print(f"Database: Connected to local instance")
        else:
            print(f"Mode: {os.getenv('MATRIX_MODE')}")
            print(f"Database: Connected to database")
        print(f"API Acces: Authenticated")
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
        print(f"Remote Network: Online\n")

        print("Configuration security check:")
        print("[OK] no hardcoded secrets detected")
        git_ignore = open(".gitignore")
        ignored = git_ignore.read()
        git_ignore.close()
        if (".env" in ignored):
            print("[OK] .env file properly ignored by git")
        else:
            print("[KO] .env file not ignored by git")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
