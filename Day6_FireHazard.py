def accionaLuces(coord1, coord2, accio):
    coord1x = int(coord1[0])
    coord1y = int(coord1[1])
    coord2x = int(coord2[0])
    coord2y = int(coord2[1])
    print('Accion:', accio,'sobre',coord1x,coord1y,'i',coord2x,coord2y)
    cont=0
    for i in range(coord1x,coord2x+1):
        cont += 1
        for j in range(coord1y,coord2y+1):
            if accio == 'A':
                a1 = matriz[i]
                a1[j] = 'A'
            if accio == 'E':
                a1 = matriz[i]
                a1[j] = 'E'
            if accio == 'T':
                a1 = matriz[i]
                if a1[j] == 'A':
                    a1[j] = 'E'
                elif a1[j] == 'E':
                    a1[j] = 'A'
    return cont

parte = int(input('Qué parte quieres ejeuctar? (1 - 2)'))
if parte == 2:
    partTwo = True
else:
    partTwo = False
    matriz = []
    listaY = []

    for i in range(1000):
        matriz.append([])
    for m in matriz:
        for j in range(1000):
            m.append('A')

with open('Day6Input.txt') as f:
    for line in f:
        word = line.rstrip()
        if partTwo:
            None
        else:
            data = word.split(" ")
            if(data[0]=='toggle'):
                coord1=data[1].split(',')
                coord2=data[3].split(',')
                accio = 'T'
                accionaLuces(coord1, coord2, accio)
            else:
                coord1 = data[2].split(',')
                coord2 = data[4].split(',')
                if(data[1] == 'on'):
                    accio = 'E'
                else:
                    accio = 'A'
                accionaLuces(coord1, coord2, accio)
    cont=0
    for m in matriz:
        cont += m.count('E')
    print(cont)