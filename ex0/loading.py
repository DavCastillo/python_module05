#!/usr/bin/env python3

from importlib.metadata import version
import importlib


def main() -> None:
    dependencies = ["pandas", "numpy"]
    missing = False
    for dep in dependencies:
        try:
            importlib.import_module(dep)
        except ModuleNotFoundError:
            missing = True
            print(f"Missing dependency: {dep}")

    if missing:
        print("Use pip or poetry to install missing dependencies:")
        print("pip: Run 'pip install -r requirements.txt'")
        print("poetry: if you don't have poetry run 'pip install poetry'"
              " then run 'poetry install', and "
              "'poetry run python loading.py'")
        return

    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    print("[OK] pandas", version("pandas"), "- Data manipulation ready")
    print("[OK] numpy", version("numpy"), "- Numerical computation ready")
    print("\npip vs Poetry: requirements.txt declares what to install; "
          "pip resolves it at install time. pyproject.toml declares the same"
          " constraints, and Poetry pins the resolved versions in poetry.lock"
          " so every install is identical.\n")
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
