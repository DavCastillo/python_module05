import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accesing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end='')
    alchemy.create_air()
    print("Air element created")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(alchemy.create_earth())


if __name__ == "__main__":
    main()
