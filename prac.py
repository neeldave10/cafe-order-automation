class cafe:
    def __init__(self):
        print("welcome to neel's cafe")

    def coffee(self,choice):
        self.choice=choice
        if choice==1:
            print("Espresso_Coffee")
        elif choice==2:
            print("Cappuccino_Coffee")
        elif choice==3:
            print("Latte_Coffee")
        else:
            print("tea")

    def tea(self,choice):
        self.choice=choice
        if choice==1:
            print("Plain_Tea")
        elif choice==2:
            print("Assam tea")
        else:
            print("ginger tea")
        Cardamom_Tea=4
        Masala_Tea=5
        Lemon_Tea=6
        Green_Tea=7
        Organic_Darjeeling_Tea=8

    def Soups(self,choice):
        self.choice=choice
        if choice==1:
            print("Hot_and_Sour_Soup")
        else:
            print("veg corn")
        Tomato_Soup=3
        Spicy_Tomato_Soup=4

    def Beverages(self,choice):
        self.choice=choice
        if choice==1:
            print("Hot_Chocolate_Drink")
        elif choice==2:
            print("badam drink")
        else:
            print("Badam_Pista_Drink")

new=cafe()
c=1
t=2
s=3
b=4
order=int(input("enter order choice"))
if order==1:
    new.coffee(int(input("enter choice")))
elif order==2:
    new.tea(int(input("enter order choice")))
elif order==3:
    new.Soups(int(input("enter order choice")))
elif order==4:
    new.Beverages(int(input("enter order choice")))
else:
    print("incorrect input")