import re

def menu():
    l=['1. Soup and salad','2. Pasta with meat sauce','3. Chef\'s special','4. Pizza','5. Brownie','6. Ice cream']
    print(*l, sep = "\n")
    n=float(input('Which number would you like to order?'))
    n=float(n)
    while n<1 or n>len(l) or n%1!=0:
        n=float(input('Sorry, that is not a valid choice.\nPlease re-enter:'))
    
    print('One'+re.findall(r'\s.+',l[int(n)-1])[0]+' coming right up! ')
    
menu()