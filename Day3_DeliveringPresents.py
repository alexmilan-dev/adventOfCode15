
d1 = [[0,0]]
x = 0
y = 0
x_robo = 0
y_robo = 0
cont=0
parte = int(input('Que parte quieres probar? (1 o 2)'))
if parte == 2:
    partTwo = True
else:
    partTwo = False

with open('Day3Input.txt', 'r') as f:
    contenido = f.read()
    for i in contenido:

        if partTwo:
            if cont%2 == 0:
                if(i=='^'):
                    y -= 1
                elif(i=='v'):
                    y += 1
                elif(i=='<'):
                    x -= 1
                elif(i=='>'):
                    x += 1
                print(i)
                print('x=',x)
                print('y=', y)

                coord_act = [x,y]

                if coord_act in d1:
                    None
                else:
                    print("inserta",coord_act)
                    d1.append(coord_act)
            else:
                if(i=='^'):
                    y_robo -= 1
                elif(i=='v'):
                    y_robo += 1
                elif(i=='<'):
                    x_robo -= 1
                elif(i=='>'):
                    x_robo += 1

                print(i)
                print('x_robo=',x_robo)
                print('y_robo=', y_robo)

                coord_act = [x_robo,y_robo]

                if coord_act in d1:
                    None
                else:
                    print("inserta robo", coord_act)
                    d1.append(coord_act)
        else:
            if (i == '^'):
                y_robo -= 1
            elif (i == 'v'):
                y_robo += 1
            elif (i == '<'):
                x_robo -= 1
            elif (i == '>'):
                x_robo += 1

            print(i)
            print('x_robo=', x_robo)
            print('y_robo=', y_robo)

            coord_act = [x_robo, y_robo]

            if coord_act in d1:
                None
            else:
                print("inserta robo", coord_act)
                d1.append(coord_act)
        cont +=1

print(len(d1))


