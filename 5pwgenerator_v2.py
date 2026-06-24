# updated version of pw generator i created before
import random
def validate(msg):
  while True:
    value=int(input(msg))
    if 0<= value <=6 :
        return value
    else:
        print("Number can't be -ve or greater the 6 ")
        



def generatepw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    passwordkeys = []

    nr_letters = validate("How many letters would you like in your password?\n")

    nr_symbols = validate("How many symbols would you like?\n")

    nr_numbers = validate("How many numbers would you like?\n")


    for i in range(0, nr_letters):
        choosen_letters = random.choice(letters)
        passwordkeys.append(choosen_letters)
    for i in range(0, nr_symbols):
        choosen_symbols = random.choice(symbols)
        passwordkeys.append(choosen_symbols)
    for i in range(0, nr_numbers):
        choosen_numbers = random.choice(numbers)
        passwordkeys.append(choosen_numbers)

    random.shuffle(passwordkeys)
    newpassword = "".join(passwordkeys)
    return newpassword


print("Welcome to the PyPassword Generator!")

password = generatepw()
print(f"Your new password : {password}")


