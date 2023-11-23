def main ():
    print("this program illusatrating chaotic behaviour")
    x = eval(input("Enter a number between o and 1: "))
    for i in range (10):
        x = 3.9 * x * (1-x)
        print (x)

main()
