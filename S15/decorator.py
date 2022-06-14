from datetime import datetime
import time

# debug decorator

# decoratorul trebuie sa returneze o alta functie
def debuger(f):
    def inner(*args):
        print("S-a apelat functia", f.__name__ ,"la ora", datetime.now(), "pentru argumentele", args)
        start = time.time()
        print("Rezultatul apelului:", f(*args))
        stop = time.time()
        print("Apelul a durat x secune", stop - start)
        f(*args)

    return inner

@debuger
def cube_volume(edge):
    """Calculate cube volume in liters"""
    # 1 m3 = 1000 litri
    return edge ** 3 * 1000

@debuger
def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev

cube_volume(10) # debuger(cube_volume)(10)
# inner(10)
reverse(234)

# def deco(f, n):
#     print("S-a apelat functia cube_volume la ora", datetime.now(), "pentru n=", n)
#     start = time.time()
#     print("Rezultatul apelului:", f(n))
#     stop = time.time()
#     print("Apelul a durat x secune", stop - start)

# deco(cube_volume, 29)




