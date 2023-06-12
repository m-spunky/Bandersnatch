list = []

for i in range(10):
    temp = []
    for j in range(10):
        if (i == 0 or i== 9 or j == 0 or j== 9 ):
            temp.append(1)
        else:
            temp.append(0)
    list.append(temp)

for i in list:
    print(i)