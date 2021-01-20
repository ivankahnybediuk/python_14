from functools import wraps


"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"
```
def logger(func):
    pass
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
```
"""


def logger(func):
    @wraps(func)
    def wrapper(*args):
        func(*args)
        print(func.__name__ + " called with " + str(args))

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == "__main__":
    add(1, 2)
    square_all(2, 3, 5, 6, 7, 23, 45)


"""
Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
```
def stop_words(words: list):
    pass
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""
def stop_words(words: list):
    def my_decorator(func):
        @wraps(func)
        def wrap(arg_string):
            result = func(arg_string)
            for word in list(map(lambda x: x.lower(), words)):
                if word in result.lower():
                    result = result.lower().replace(word, "*")
            return result
        return wrap
    return my_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new Bmw!"


if __name__ == "__main__":
    print(create_slogan("Steve"))


"""
Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
```
def arg_rules(type_: type, max_length: int, contains: list):
    pass
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def my_decorator(func):
        @wraps(func)
        def wrap(arg_string):
            def containing():
                for symbol in contains:
                    if arg_string.find(symbol) == -1:
                        return False
                return True

            if type(arg_string) == type_ and len(arg_string) <= max_length and containing():
                return func(arg_string)
            else:
                return "Невозможно выполнить!"

        return wrap

    return my_decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    print(create_slogan("05a1Ffdddddff@"))
