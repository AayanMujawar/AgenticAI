def greet(name="Guest"):
    """Return a greeting message."""
    name = name.strip()
    if not name:
        name = "Guest"
    return f"Hello, {name}!"


def main():
    name = input("Enter your name: ")
    print(greet(name))


if __name__ == "__main__":
    main()
