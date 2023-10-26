def main():
    print("hey")
    test_func()


def decorator_func(func):
    def wrapper():
        print("hello there")
        func()
    return wrapper


@decorator_func
def test_func():
    print("heyo")


if __name__ == "__main__":
    main()
