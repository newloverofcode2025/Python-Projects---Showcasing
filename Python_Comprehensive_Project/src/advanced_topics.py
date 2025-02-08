# src/advanced_topics.py

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

def generator_example():
    for i in range(5):
        yield i

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

def main():
    print("Advanced Topics:")
    say_hello()

    print("\nGenerator Example:")
    for value in generator_example():
        print(value)

    print("\nContext Manager Example:")
    with MyContextManager():
        print("Inside the context")

if __name__ == "__main__":
    main()