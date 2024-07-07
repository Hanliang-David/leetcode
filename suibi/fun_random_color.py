# fun_random_color.py
import random

def fun_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

print(fun_random_color())
