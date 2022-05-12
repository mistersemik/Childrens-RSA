import random

#Alphabet
a1 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a2=a1.lower()
a3=' "№;%:?!@#$%^&*()_+,.[]{}\|/'
abc = a1+a2+a3


def Evklid(num1,num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def invert(x, m):
    u = (m, 1, 0)
    v = (x, 0, 1)
    while v[0]:
        q = u[0] // v[0]
        u, v = v, [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
    return u[2] % m

def find_e(e,f):
    e1 = Evklid(e, f)
    while e1 != 1:
        e = random.randint(1, f)
        e1 = Evklid(e, f)
    return e