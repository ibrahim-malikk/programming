#factorial.py
#program to calculate the factorial of a number
#illustrates for loop with an accumlator

def main():
    n = int(input("pleease enter a whole number"))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
        print("the factorial of", n, "is", fact)

main()
