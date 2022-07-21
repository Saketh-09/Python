import re
def balance():
    n=int(input('Enter no of transactions:'))
    l=[0]*n
    d=[]
    w=[]
    for i in range(n):
        l[i]=input('Enter transaction no '+str(i+1)+' (ex:D 500 or W 300) :')
        match=re.findall('\w+',l[i])
        if match[0]=='d' or match[0]=='D':
            d.append(match[1])
        elif match[0]=='w' or match[0]=='W':
            w.append(match[1])
    deposit=list(map(float,d))
    withdraw=list(map(float,w))
    return (sum(deposit)-sum(withdraw))

print('net amount of bank account is:'+str(balance()))


    
