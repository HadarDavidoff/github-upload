class FactorialArgumentError(BaseException):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "This argument %s is not an integer" % self._arg


def factorial(num):
    if int(num) == 1:
        return 1
    else:
        return int(num) * factorial(num - 1)


def main():
    x = input("Insert a number to factorial")
    try:
        factorial(int(x))
    except ValueError(x):
        print("nahh")
    except TypeError as e:
        print("notnotnot")
    else:
        print(factorial(int(x)))


if __name__=="__main__":
    main()