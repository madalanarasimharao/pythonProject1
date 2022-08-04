class calPA:
    def PArectangle(self,a,b):
        print("rectangle perimeter=",2*(a+b))
        print("Area=",a*b)

    def PAcircle(self, a):
        print("Circle perimeter=",2*3.14*a)
        print("Area=",3.14*a*a)

    def PAtriangle(self,a,b,c):
        print("Triangle perimeter",a+b+c)
        s=(a+b+c)/2
        print("Area=",s*(s+a)*(s+b)*(s+c))
class main(calPA):
    print("Select one of these to find area and perimeter\n 1.rectangle\n2.circle\n3.triangle")
    obj=calPA()
    choice=int(input("\nEnter choice: "))
    if choice==1:
        a=int(input("Enter first side:"))
        b = int(input("Enter second side:"))
        obj.PArectangle(a,b)
    elif choice==2:
        a = int(input("Enter radius of circle:"))
        obj.PAcircle(a)
    elif choice==3:
        a = int(input("Enter first side:"))
        b = int(input("Enter second side:"))
        c = int(input("Enter third side:"))
        obj.PAtriangle(a,b,c)
    else:
        print("Wrong choice")