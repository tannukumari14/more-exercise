print("creat new pasward")
print("strong password")
ch=str(input("enter the uppar case letter"))
if ch>="A" and ch<="Z":
    ch2=str(input("enter lower case letter"))
    if ch2>="a" and ch2<="z":
        num=input("enter the number")
        sc=input("enter special character")
        if sc=="@" or sc=="$" or sc=="&" or sc=="!":
            print(ch+ch2+num+sc)
        else:
            print("envailid")
    else:
        print("envailid")
else:
    print("envailid")    