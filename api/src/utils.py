from time import time_ns


def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A = a.lower()
alphabet = a + A + '1234567890-_'


def generate_shortid():
    r = ''
    for i in number_to_base(time_ns(), 64):
        r += alphabet[i]
    return r

