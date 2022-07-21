from os import getegid


def getEvenNumber(l):
    return list(filter(lambda x:x%2==0,l))


n=int(input('Enter the length of list from which "Even" numbers need to be filtered: '))
l=[]
for i in range(n):
    l.append(int(input('Enter list element number '+str(i+1)+' : ')))
print(getEvenNumber(l))