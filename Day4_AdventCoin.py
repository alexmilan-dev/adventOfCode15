import hashlib
from datetime import datetime
parte = int(input('Qué parte quieres ejeuctar? (1 - 2)'))
if parte == 2:
    partTwo = True
else:
    partTwo = False
print(datetime.now())
key = 'iwrupvqb'
encontrado = False
num = 1

while(encontrado == False):
    codi = key+str(num)
    md5 = hashlib.md5(codi.encode())
    cadena = md5.hexdigest()
    if partTwo:
        pos = cadena.find("000000")
    else:
        pos = cadena.find("00000")

    if pos == 0:
        encontrado = True
        print(codi)
        print(md5.hexdigest())
        print(datetime.now())

    num += 1