def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    name = input("Enter your name: ").strip()

    if name:
        print(greet(name))
    else:
        print("Hello, Guest!")


if __name__ == "__main__":
    main()
