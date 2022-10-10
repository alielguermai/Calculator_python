def addition(x,y):
    return int(x) + int(y)
def soustraction(x,y):
    return int(x)-int(y)
def division(x,y):
    return int(x)/int(y)
def multiplication(x,y):
    return int(x)*int(y)
restart ="yes"
while restart=="yes":
    print("Choose the operation:")
    print("Type + for addition")
    print("Type - for substraction")
    print("Type / for division")
    print("Type * for multiplication")
    type = input("Type here ---> ")
    while type != "+" and type != "-" and type != "/" and type != "*":
        print("ERROR")
        type = input(" type again -->")
    x = input("Enter the first number:")
    while x.isnumeric() == False:
        print("ERROR")
        x = input("Enter again: ")
    y = input("Enter the second number:")
    while y.isnumeric() == False:
        print("ERROR")
        y = input("Enter again: ")
    if type == "-":
        print("The result is: " + str(soustraction(x,y)))
    elif type == "/":
        print("The result is: " + str(division(x,y)))
    elif type == "*":
        print("The result is: " + str(multiplication(x,y)))
    elif type == "+":
        print("The result is: " + str(addition(x,y)))
    restart = input("Do you want to restart? Type yes or no: ")
    if restart =="no":
        print("OK")