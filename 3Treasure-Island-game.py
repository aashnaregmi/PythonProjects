print("Welcome to Treasure Island 🏝️")
print("Your mission is to find the treasure.")
print("You are at the cross road")
direction1=input("Where do you want to go Left or Right (L or R) ?").lower()

if direction1=="l":
    d2=input("Do you want to swim or wait (S,W)? ").lower()
    if d2=="w":
        d3=input("Which door do you want to go (Yellow,Blue,Red)?").lower()
        if d3=="yellow":
            print("You win!")
        elif d3=="red":
            print("Burned by fire.\nGame over")
        elif d3=="blue":
            print("Eaten by beasts.\nGame over")
        else:
            print("Game over")
    else:
        print("Attacked by trout.\nGame over")
else:
    print("Fall into hole.\nGame over.")


