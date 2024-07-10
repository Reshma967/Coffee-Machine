MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
a=True
water=300
milk=200
coffee=100
money=0
while(True):
    choice=input("What would you like? espresso/latte/cappuccino:")
    if (choice == "report"):
        print("Water:",resources["water"])
        print("Milk:",resources["milk"])
        print("Coffee:",resources["coffee"])
        print("Money:",money)
        choice = input("What would you like? espresso/latte/cappuccino:")
    print("Please insert coins")
    q=int(input("How many quarters?:"))
    d=int(input("How many dimes?:"))
    n=int(input("How many nickels?:"))
    p=int(input("How many pennies?:"))
    pvalue = p*0.01
    dvalue = d*0.10
    nvalue = n*0.05
    qvalue = q*0.25
    coste = MENU["espresso"]["cost"]
    costl = MENU["latte"]["cost"]
    costc = MENU["cappuccino"]["cost"]
    paid=pvalue+dvalue+nvalue+qvalue
    change=0
    if(choice=="espresso"):
        if(paid >= coste):
            change=paid-coste
            change=round(change,2)
            print(f"Here is ${change} in change")
            print(f"Here is your {choice}. Enjoy!")
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["milk"] = resources["milk"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            money += 1.5
        else:
            print("money not enough")
    elif(choice=="latte"):
        if (paid >= costl):
            change = paid - costl
            change = round(change,2)
            print(f"Here is ${change} in change")
            print(f"Here is your {choice}. Enjoy!")
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            money += 2.5
        else:
            print("money not enough")
    elif(choice=="cappuccino"):
        if (paid >= costc):
            change = paid - costc
            change=round(change,2)
            print(f"Here is ${change} in change")
            print(f"Here is your {choice}. Enjoy!")
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"]  = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"]  = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            money += 3
        else:
            print("money not enough")

