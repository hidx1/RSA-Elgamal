def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def writeToFile(data, mode):
    if (mode == 0):
        f = open("public.pub", "w")
    else:
        f = open("private.pri", "w")

    f.write(data)
    f.close()


def diffie_helman(n, g, x, y):
    return pow((pow(g, x) % n), (pow(g, y) % n)) % n
