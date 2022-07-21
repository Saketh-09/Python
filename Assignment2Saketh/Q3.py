def evaloddeven(n):
    if n%2==0:
        return 'Given input is an "Even" integer'
    else:
        return 'Given input is an "Odd" integer'
n=float(input('Enter the integer:')) 
while n%1!=0:
    n=float(input('Input is not an integer, please re-enter:'))
print(evaloddeven(n))