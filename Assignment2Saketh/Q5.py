def averages(l):
    avg=[0]*3
    n=len(l)
    frequency=[0]*n
    sum=0
    
    for i in range(n):
        sum+=l[i]
        j=i-1
        while j>=0:
            if l[i]==l[j]:
                frequency[i]=frequency[j]+1
                break
            j=j-1
        if frequency[i]>=max(frequency):
            modeind=i
    avg[0]=sum/n
    if n%2==0:
        avg[1]=(l[n//2]+l[n//2-1])/2
    elif n%2==1:
        avg[1]=l[n//2]
    avg[2]=l[modeind]
    return avg;
series=input('Enter series with spaces in between (ex:1 2 3 4.5):\n').split()
avgs=averages(list(map(float,series)))
print('Mean of the series is :'+str(avgs[0]))
print('Median of the series is :'+str(avgs[1]))
print('Mode of the series is :'+str(avgs[2]))
            