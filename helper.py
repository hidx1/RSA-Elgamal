import os

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
    elif (mode == 1):
        f = open("private.pri", "w")
    else:
        f = open("cipherText.ecr", "w")

    f.write(data)
    f.close()

def readFromFile(file_name):
    extension = os.path.splitext(file_name)[1]
    data = None
    is_cipherText = False
    if extension == ".ecr":
        is_cipherText = True
        f = open(file_name, "r")
        data = f.read()
    else:
        f = open(file_name, "rb")
    f.close()
    return data, is_cipherText

def codeMessage(msg):
    result = ""
    for char in msg:
        code = str(ord(char))
        headingLength = 3-len(code)
        for i in range(headingLength):
            code = '0'+code
        result += code
    if (len(result) % 6 != 0):
        result += "256"
    return result

def diffie_helman(n, g, x, y):
    return pow(pow(g, x, n), y, n)

def gcd(p, q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

if __name__ == "__main__":
    for i in range(1000000000000000000000000000000000000000000000000000000000000000000000000000):
        if (is_coprime(i, 1210145036063417205622974722189679300425594239971785447214628764089958055217275328377339625440400256608307406736692769091333622175530734487728425224810942804559270668428759323294557805268314468224293367130593570261803241958640659109949848064843598016986040681231330709222324227117155849109075659061411541132721)):
            print(i)
