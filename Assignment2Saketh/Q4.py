def squares():
    l=[]
    for i in range(1,21):
        l.append(i**2)
        if i>15:
            print(l[i-1])
                
squares()
    