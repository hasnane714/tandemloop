print("\n CALCULATOR\n")
print("\n \t NOTE: int data  type in python3 has no limit on the maximum value so there's no use of  double in python3")

class calculator:
    
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a  *  self.b
    def div(self):
        return self.a  /  self.b

a=input("\n ENTER VALUE OF A: ")
b=input("\n ENTER VALUE OF B: ")
obj=calculator(a,b)

choice=1
while choice !=0:
    print("\n0. EXIT")
    print("1. ADDITION")
    print("2. SUBSTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    choice=int(input("ENTER YOUR CHOICE: "))
    if choice==1:
        print("the addition is ",obj.add())
    elif choice==2:
        print("the substraction is ", obj.sub())
    elif choice==3:
        print("the multiplication is ", obj.mul())
    elif choice==4:
        print("the division is ", obj.div())
    elif choice==0:
        print("EXITING......")
    else:
        print("choice invalid !!!")
print()
