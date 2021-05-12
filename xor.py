# ajoute deux binaires avec la logique xor pour donner un nouveau binaire qui pourra être utiliser pour le chiffrement
def add_bin(b1, b2):
    result = ''
    for i in range(8):
        if (b1[i] == '1') and (b2[i] == '1'):
            result += '0'
        elif (b1[i] == '0') and (b2[i] == '1'):
            result += '1'
        elif (b1[i] == '1') and (b2[i] == '0'):
            result += '1'
        elif (b1[i] == '0') and b2[i] == '0':
            result += '0'
    return result

# ma propre fonction qui remplace la fonction native bin pour passer un entier en binaire sur 8 bits
def to_bin(number):
    temp = []
    result = ''
    while number // 2 != 0:
        number = number // 2
        temp.append(number % 2)
    if len(temp) < 8:
        for i in range(1, 8 - len(temp)):
            temp.append(0)
    temp = temp[::-1]
    temp.append(0)
    for i in range(len(temp)):
        result = result + result.join(str(temp[i]))
    return result

# Ma propre fonction pour passer de binaire à de decimal
def to_dec(number):
    puissance = [1, 2, 4, 8, 16, 32, 64, 128]
    number = number[::-1]
    resultat = 0
    for i in range(8):
        if number[i] == '1':
            resultat = resultat + puissance[i]
    return int(resultat)


"""
Other function found on internet to check if mine was good 

def to_dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != '0'):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return dec
"""


def xor(mot, cle):
    result = ''
    key_len = (((len(mot) - len(cle)) // len(cle)) * len(cle)) + ((len(mot) - len(cle)) % len(cle)) # calcul complexe pour chopper la bonne taille de la clé
    for i in range(key_len):
        cle = cle + cle[i]
    for i in range(len(mot)):
        result += add_bin(to_bin(ord(mot[i])), to_bin(ord(cle[i])))  # + ' ' for more readability
    return result


def un_xor(binaire, cle):
    key_len = (((len(binaire) - len(cle)) // len(cle)) * len(cle)) + ((len(binaire) - len(cle)) % len(cle)) # calcul complexe pour chopper la bonne taille de la clé
    key_len = key_len // 8 # diviser par 8 car on est sur un octet
    result = ''
    resultat = ''
    iteration = 8
    iteration2 = 8
    j = 0
    print(f"Binaire de base : {binaire}")
    for i in range(0, key_len + 1):
        cle = cle + cle[i]
    print(cle)
    while iteration2 <= len(binaire):
        resultat += add_bin(binaire[iteration2 - 8: iteration2], to_bin(ord(cle[j])))
        print("Add_bin (mon xor fait en suivant la table de vérité) : " + str(to_dec(add_bin(binaire[iteration2 - 8: iteration2], to_bin(ord(cle[j]))))))
        print("xor : " + str(to_dec(binaire[iteration2 - 8: iteration2]) ^ ord(cle[j])))
        print()
        j += 1
        iteration2 += 8
    while iteration < len(binaire):
        result += chr(to_dec(resultat[iteration - 8: iteration]))
        iteration += 8
    return result

# Chiffrement de informatique avec la clé
print(xor("informatique", "nsi"))

# Déchiffrement de informatique en suivant la logique [messagedebase + clé = messagechiffré] <=> [messagechiffré + clé = messagedebase]
print(un_xor(xor("informatique", "nsi"), "nsi"))

