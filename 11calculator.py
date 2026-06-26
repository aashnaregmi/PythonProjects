def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

operator={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide,

}

while True:
    n1=float(input("Enter the 1st num: "))
    while True:
        operation=input("Enter the operation (+,-,*,/): ")
        n2=float(input("Enter the 2nd num: "))
        for key in operator:
            if key == operation:
                call = operator[key]
                output=call(n1, n2)
                print(f"The output is {output}")
        continuewithans=input("Type 'y' to continue with the output else 'n'")
        if continuewithans=="n":
            break
        elif continuewithans=='y':
             n1=output
             continue
        else:
            print("Enter correct operation")
            break







