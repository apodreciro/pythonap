v = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
u = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

for i in range (0,4):
    for j in range (0,4):
        v[i][j] = int(input(f"escolha o valor [{i+1}, {j+1}]da matriz: "))

for i in range (0,4):
    for j in range (0,4):
        u[i][j] = int(input(f"escolha o valor [{i+1}, {j+1}]da matriz: "))

for i in range (0,4):
    for j in range (0,4):
        print(u[i][j]+v[i][j], end = ' ')


    print()

