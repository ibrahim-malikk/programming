#change.py
# calculate the value of change into dollars

def main():
    print("change counter")
    print()
    print("please enter the count of each coin type.")
    quarters = eval(input("quarters: "))
    dimes = eval(input("dimes: "))
    nickles = eval(input("nickles: "))
    pennies = eval(input("pennies: "))
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    print()
    print("the total value of your change is", total)

main()
