# generator/password_generator.py
import random
import string

def password_generator(length=12, symbols=True):
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))
