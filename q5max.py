a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"max")
elif b>c and b>a:
    print(b,"max")
elif c>b and c>a:
    print(c,"max")