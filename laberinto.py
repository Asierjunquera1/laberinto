def laberinto():
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
    lab=[]
    for i in range(5):
        fila=[]
        for j in range(5):
            a=(i, j)
            if a in muro:
                fila.append('x')
            else:
                fila.append(' ')
        lab.append(fila)
    return lab


for i in range(5):
    print(laberinto()[i])

