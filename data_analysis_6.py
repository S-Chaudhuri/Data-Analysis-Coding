#highest of 3 numbers
#if-else concept used

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))
if a>=b and b>=c:
    print(c,"<=",b,"<=",a)
elif b>=a and a>=c:
    print(c,"<=",a,"<=",b)
elif c>=a and a>=b:
   print(b,"<=",a,"<=",c)
elif a>=c and c>=b:
    print(b,"<=",c,"<=",a)
elif b>=c and c>=a:
    print(a,"<=",c,"<=",b)
elif c>=a and a>=b:
   print(b,"<=",a,"<=",c)
elif c>=b and b>=a:
    print(a,"<=",b,"<=",c)
