import math
a= input('Enter a')
b= input('Enter b')
c= input('Enter c')
delta = int(b)**2 - 4*int(a)*int(c)
if delta >0 :
    x1= -int(b) - math.sqrt(delta)/2*int(a)
    x2= -int(b) + math.sqrt(delta) / 2 * int(a)
    print('the equation has two solutions :')
    print('x1 = ',x1)
    print('x2 = ',x2)
elif delta ==0:
    x= -int(b)/2*int(a)
    print('The equation has one unique solution :')
    print('x = ',x)
else :
    print('The equation has no solutions')

