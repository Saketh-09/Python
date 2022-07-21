def func1(x,y):
    l=[]
    for i in range(x,y+1):
        if i%2==0:
            l.append(i)
    return l
x=int(input('Enter the starting number in the range(inclusive): '))
y=int(input('Enter the ending number in the range(inclusive): '))
print(func1(x,y))