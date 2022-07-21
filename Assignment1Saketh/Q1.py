def maxindval(l):
    maxval=max(l)
    maxind=l.index(maxval)
    print(l.pop(maxind))
    return l
l=[]
for i in range(10):
    l.append(int(input('Enter +ve integer no '+str(i+1)+' :')))
print 'Below showing the input in descending order'
for i in range(10):
    maxindval(l)