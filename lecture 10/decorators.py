def main():
    print("hey")
    # test_func != test_func()
    test_func()
    test_func2()


def decorator_func(func):
    def wrapper():
        func()
    return wrapper


@decorator_func
def test_func():
    print("heyo")


@decorator_func
def test_func2():
    print("hi again")


if __name__ == "__main__":
    main()
