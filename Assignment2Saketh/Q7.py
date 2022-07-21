def  sortTuple():
    n=int(input('Enter the no of tuples you want to sort:'))
    l=[]
    templ=[]
    for i in range(n):
        a=input('Enter tuple number '+str(i+1)+' :')
        templ=a.split(',')
        a=tuple(templ)
        
        for j in range(len(l)):
            if l[j][0]>a[0]:
                l.insert(j,a)
                break
            elif l[j][0]==a[0]:
                if l[j][1]>a[1]:
                    l.insert(j,a)
                    break
                elif l[j][1]==a[1]:
                    if l[j][2]>a[2]:
                        l.insert(j,a)
                        break
        if len(l)!=i+1:
            l.append(a)            
            
    return l
    
print(sortTuple())

                