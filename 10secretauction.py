print("\n")
print("====WELCOME TO AUCTION PROGRAM====")
print("\n")

continueloop = "yes"
auction_info = []
largest = {
    "name": "",
    "bid": 0,
    "index": 0
}

while True:
    name = input("Enter your name : ").capitalize()
    bid = int(input("Enter the bid :$"))

    auction_info.append({
        "name": name,
        "bid": bid,
    })

    while True:#for no is error
        continueloop = input("More people 'yes' or 'no '?").lower()

        if continueloop == "yes":
            print("\n" * 30)
            break  # go back to main loop

        elif continueloop == "no":
            totalpeople = 1

            for i in range(0, len(auction_info)):

                if auction_info[i]['bid'] > largest["bid"]:
                    largest["bid"] = auction_info[i]['bid']
                    largest["name"] = auction_info[i]['name']
                    largest["index"] = i

            for i in range(0, len(auction_info)):
                if i != largest["index"] and auction_info[i]['bid'] == largest["bid"]:
                    totalpeople += 1

            print("=========================================================")

            if totalpeople == 1:
                print(f"      The highest bid is of \"{largest['name']}\" for ${largest['bid']}!!")
            else:
                print(
                    f"     It's a tie!! \n     The highest bid is  ${largest['bid']} which was bid by {totalpeople} people "
                )

            print("==========================================================")
            exit()

        else:
            print('Enter "yes" or "no"')