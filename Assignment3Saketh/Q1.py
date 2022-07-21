import math
def roots():
    a=float(input('Enter coefficient of x^2 (a), (where eqn in form: ax^2+bx+c): '))
    b=float(input('Enter coefficient of x (b), (where eqn in form: ax^2+bx+c): '))
    c=float(input('Enter constant(c), (where eqn in form: ax^2+bx+c): '))
    if b**2-4*a*c<0:
        print('The quadratic equation has complex roots')
    else:
        r1=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        r2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print(str(r1)+', '+str(r2)+' are the roots of the given quadratic equation')
roots()