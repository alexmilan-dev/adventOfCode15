

with open('Day1Input.txt', 'r') as f:
    contenido = f.read()

floor=0
cont=0
res = 0
for i in contenido:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    if floor == -1 and res == 0:
        res = cont+1
    cont += 1

print(res)

