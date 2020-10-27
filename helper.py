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

def writeKeyToFile(data, mode):
    if (mode == 0):
        f = open("public.pub", "w")
    else:
        f = open("private.pri", "w")
    
    f.write(data)
    f.close()

def writeCodeToFile(codedText):
    f = open("cipherText.txt", "w")
    result = ""
    for i in range(int(len(codedText)/3)):
        print(f"i: {i}")
        block = codedText[i*3:i*3+3]
        print(f"block: {block}")
        char = chr(int(block))
        result += char
    print(f"result: {result}")
    f.write(char)
    f.close()

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