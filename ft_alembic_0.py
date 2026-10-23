import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire: ", end='')
    elements.create_fire()
    print("Fire element created")


if __name__ == "__main__":
    main()
