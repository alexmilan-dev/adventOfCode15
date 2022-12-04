def contieneTresVocales(word):
    vocales = 0
    for c in word:
        if c in 'aeiou':
            vocales += 1
            if vocales == 3:
                return True
    return False

def contieneGemela(word):
    c_ant = ''
    for c in word:
        if c == c_ant:
            return True
        c_ant = c
    return False

def contieneCombProhibida(word):
    ## Crear tupla con valore prohibidos
    ## recorrer todos los prohibidos de la tupla y determinar si existe alguno o no
    prohibidos = ('ab','cd','pq','xy')
    for p in prohibidos:
        if p in word:
            return True
    return False

def contieneSandwitch(word):
    for i in range(len(word)):
        if i < len(word)-2:
            if word[i] == word[i+2]:
                return True
    return False

def buscarCuatro(word, i):
    for c in word:
        cadena=c+c+c+c
        print(cadena)
        enc=word.find(cadena)
        if enc > -1:
            return 1
    return 0

def contieneParRepetido(word):
    for i in range(len(word)):
        if i < len(word)-2:
            if i == 0:
                par=word[i]+word[i+1]
                cerca = word.find(par)
                if cerca == -1:
                    None
                else:
                    if cerca == i:
                        cerca2 = word.find(par, i+1)
                        if cerca2 != -1:
                            if cerca2 == i+1:
                                cadena = word[i] + word[i] + word[i] + word[i]
                                if (par[0] == par[1]):
                                    enc = word.find(cadena)
                                    if enc > -1:
                                        print(word,'1')
                                        return True
                                    else:
                                        cerca3 = word.find(par, i + 2)
                                        if cerca3 != -1:
                                            print(word, '5b')
                                            return True
                            else:
                                print(word, '2')
                                return True
                    elif (cerca == i+1):
                        cadena = word[i]+word[i]+word[i]+word[i]
                        if (par[0] == par[1]):
                            enc = word.find(cadena)
                            if enc > -1:
                                print(word, '3')
                                return True
                            else:
                                cerca3 = word.find(par, i + 2)
                                if cerca3 != -1:
                                    print(word, '5b')
                                    return True
                    else:
                        print(word, '4')
                        return True
            else:
                par = word[i] + word[i + 1]
                cerca = word.find(par)
                if cerca == -1:
                    None
                elif cerca == i:
                    cerca2 = word.find(par,i+1)
                    if cerca2 != -1:
                        if cerca2 == i+1:
                            cadena = word[i] + word[i] + word[i] + word[i]
                            if (par[0] == par[1]):
                                enc = word.find(cadena)
                                if enc > -1:
                                    print(word, '5')
                                    return True
                                else:
                                    cerca3 = word.find(par,i+2)
                                    if cerca3 != -1:
                                        print(word, '5b')
                                        return True
                        else:
                            print(word, '6')
                            return True
                elif(cerca == i+1):
                    cadena = word[i] + word[i] + word[i] + word[i]
                    if (par[0] == par[1]):
                        enc = word.find(cadena)
                        if enc > -1:
                            print(word)
                            print(word, '7')
                            return True
                elif(cerca == i-1):
                    None
                else:
                    print(word, '8')
                    return True
    return False

parte = int(input('Qué parte quieres ejeuctar? (1 - 2)'))
if parte == 2:
    partTwo = True
else:
    partTwo = False

cont = 0

with open('Day5Input.txt') as f:
    for line in f:
        word = line.rstrip()
        if partTwo:
            if (contieneSandwitch(word)) and contieneParRepetido(word):
                cont = cont+1
        else:
            if contieneTresVocales(word) and contieneGemela(word) and not contieneCombProhibida(word):
                cont = cont+1

    print(cont)
