recources_needed={
  "espresso":{
         "water":50,
         "milk":0,
         "coffee":18,
         "cost":1.50
         
    
  },
  "latte":{
         "water":200,
         "milk":150,
         "coffee":24,
         "cost":2.50
         
    
  },
  "cappuccino":{
         "water":250,
         "milk":100,
         "coffee":24,
         "cost":3.00
    
  }
  
}

resources_available = {
    "water": 400,   
    "milk": 400,    
    "coffee": 100,   
}
money=0.0

coins={
  "quarter":0.25,
  "dime":0.10,
  "nickel":0.05,
  "penny":0.01,
  
  
}
def welcome_msg():
  print("=" * 45)
print("      ☕ WELCOME TO COFFEE MACHINE ☕")
print("=" * 45)

print("\nHello! What would you like today?\n")

print("📋 MENU")
print("-" * 45)
print("☕ Espresso      - $1.50")
print("🥛 Latte         - $2.50")
print("☕🥛 Cappuccino   - $3.00")
print("-" * 45)

print("\nCommands:")
print("• espresso")
print("• latte")
print("• cappuccino")
print("• report  - View machine resources")
print("• off     - Turn off the coffee machine")
print("=" * 45)


    

    
#5   
def report_status():
    for key in resources_available:
        print(f"{key}: {resources_available[key]}")
    print(f"money :{money}")
# 4
def calculate_money(order,amt_received):
    order_amt=recources_needed[order]["cost"]
    if order_amt>amt_received:
        print("The amount is not sufficient!!")
        
        return
     
    elif order_amt<amt_received:
         returnmoney=round(amt_received-order_amt,2)
         print(f"The returned amount :{returnmoney}")
         print("Enjoy your order!!")
         money=round(amt_received -returnmoney,2)
         return money
    else:
         money=amt_received
         print("Enjoy your order!!")
         return money
            
    
#3rd
def ask_coin():
    print("\nPlease insert coins.")
    quarters_amt = float(input("How many quarters?: "))
    dimes_amt = float(input("How many dimes?: "))
    nickels_amt= float(input("How many nickels?: "))
    pennies_amt = float(input("How many pennies?: "))  
    total_amt = (
    quarters_amt * coins["quarter"] +
    dimes_amt * coins["dime"] +
    nickels_amt * coins["nickel"] +
    pennies_amt * coins["penny"]
)   
    total_amt=round(total_amt,2)
    print(f"The total amount received is {total_amt}")
    return total_amt
    
    
#2nd
def process_order(order):
    if order == "report":
       report_status()
       return
       
    resources_status=check_resources(order)
    if resources_status =="enough":
       total_amt_received= ask_coin()
       money_got=calculate_money(order,total_amt_received)
       return money_got
#1st     
def check_resources(order):
  for key in resources_available:
    if recources_needed[order][key]>resources_available[key]:
        print(f"Sorry there is not enough {key}.")
        break
  else:
        return "enough"
    
    

while True:
  welcome_msg()
  order=input("What is your order(Espresso,Latte,Cappuccino)?").lower()
  received=process_order(order)
  if received!=None:
     money+=received
  
  
  
  
  
 

  