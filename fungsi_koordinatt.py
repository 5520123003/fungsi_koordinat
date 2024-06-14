import math
range_pharsa = 2

x = 10
y = 10

def cek_hidup_mati(R,S):
    a = R - x
    b = S - y
    c = math.sqrt(a*a + b*b)
    print(c)

    if c <= range_pharsa:
        print("MATI")

    else:
        print("HIDUP")

cek_hidup_mati(20,20)