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
    if (mode == 0): #write public key file
        f = open("public.pub", "w")
    elif (mode == 1): #write private key file
        f = open("private.pri", "w")
    else: #write ciphertext file
        f = open("cipherText.ecr", "w")

    f.write(data)
    f.close()

def writePlainText(byteArray, file_name):
    result = bytes(byteArray)
    f = open(file_name, "wb")
    f.write(result)
    f.close()


def readFromFile(file_name):
    extension = os.path.splitext(file_name)[1]
    data = None
    is_cipherText = False
    if extension == ".ecr":
        is_cipherText = True
        f = open(file_name, "r")
        data = f.read()
    elif extension == ".pub" or extension == ".pri":
        f = open(file_name, "r")
        data = f.read()
        splitted = data.split(",")
        return int(splitted[0]), int(splitted[1])
    else:
        f = open(file_name, "rb")
        data = []
        byte = f.read(1)
        while byte:
            data.append(ord(byte))
            byte = f.read(1)
    f.close()
    return data, is_cipherText


def codeMessage(msg, mode):
    result = ""
    for data in msg:
        if (mode == 0):
            code = str(ord(data))
        else:
            code = str(data)
        paddingLength = 3 - len(code)
        padding = '0' * paddingLength
        code = padding + code
        result += code
    
    # if (len(result) % 6 != 0):
    #     result += "256"

    return result


def diffie_helman(n, g, x, y):
    return pow(g, x * y, n)


def el_gamal_encrypt():
    return


def el_gamal_decrypt():
    return


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1