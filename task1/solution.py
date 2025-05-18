def strict(func):
    def wrapper(*args):
        func_args = func.__annotations__
        for arg, v in zip(args, func_args.values()):
            if type(arg) != v:
                raise TypeError(f"Неверный тип аргумента.")
        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
