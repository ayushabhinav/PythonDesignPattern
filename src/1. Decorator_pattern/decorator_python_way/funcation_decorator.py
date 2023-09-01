import random


def my_business_code():
    result = random.randint(0, 10) ** 2
    return result


def generate_log(fun):
    print("*" * 20)
    print("i am from generate log")
    res = fun()
    print(f"output:{res}")
    print("*" * 20)
    return res


res = my_business_code()
print(f"Result from my_business_code:{res}")

print(" FUNCATION DECORATION ")

res = generate_log(my_business_code)
print(f"Result from generate_log:{res}")


######################################## @ notation of using the decorator ###########################


def gen_log(func):
    def inner():
        res = func()
        print(f"result is :{res}")
        return res

    return inner


@gen_log
def my_business_code_2():
    result = random.randint(1, 10) ^ 3
    return result


res = my_business_code_2()
print(f"Result from my_business_code_2:{res}")


################################## passing parameters to inside funcation ######################################


def gen_log_2(func):
    def inner(*args, **kwargs):
        print(args)
        print(kwargs)
        res = func(*args, **kwargs)
        print(f"result is:{res}")
        return res

    return inner


@gen_log_2
def my_business_code_3(a, b):
    result = random.randint(1, 10) ^ 3
    return result


res = my_business_code_3(4, 5)
print(f"Result from my_business_code_3:{res}")


##################################### passing parameters to decorator ############################################


def upper_decorator(schema="ALL"):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("*" * 20)
            print(f"args:{args}")
            print(f"kwargs:{kwargs}")
            res = func(*args, **kwargs)

            if schema == "ALL":
                res = res.upper()

            if schema == "ONLY_FIRST":
                res = res.capitalize()

            if schema == "EACH_FIRST_LETTER":
                res = " ".join([w.capitalize() for w in res.split()])

            print(f"result:{res}")
            print("*" * 20)
            return res

        return inner_wrapper

    return wrapper


@upper_decorator(schema="EACH_FIRST_LETTER")
def greetings(name):
    return f"hello {name}, how are you doing?"


res = greetings("ayush")
print(res)

print(f"greeting function name is :{greetings.__name__}")


############################################## using func tools wraps ####################################

from functools import wraps


def decortor_fn(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("*" * 20)
        print(f"args:{args}")
        print(f"kwargs:{kwargs}")
        res = func(*args, **kwargs)
        print(f"result:{res}")
        print("*" * 20)
        return res

    return wrapper


@decortor_fn
def origial_fn():
    print("Hi")


origial_fn()
print(f"original_fn_name:{origial_fn.__name__}")
