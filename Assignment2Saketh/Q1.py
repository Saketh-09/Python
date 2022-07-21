import re
str=input('Enter the mathematic expression: ')
a=re.findall('[\w.]+',str)
operator=re.findall('\S',str)
for i in operator:
    if not i.isdigit() and i!='.':
        char=i
if char=='+':
    print(float(a[0])+float(a[1]))
elif char=='*':
    print(float(a[0])*float(a[1]))
elif char=='/':
    print(float(a[0])/float(a[1])) 
elif char=='-':
    print(float(a[0])-float(a[1])) 