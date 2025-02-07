def caesarCipher(s, k):
    # s = string
    # k = number of shifts

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""
    n = len(alphabets)
    shift = k % n

    for a in s:
        if a.isalpha():
            index = alphabets.index(a.lower()) + shift
            if index > 25:
                index = index - n

            CHAR = ALPHABETS if a.isupper() else alphabets
            cipher += CHAR[index]

        else:
            cipher += a

    return cipher


print(caesarCipher("abc", 24))  # yza
print(caesarCipher("middle-Outz", 2))  # okffng-Qwvb
