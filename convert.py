#convert.py
# A program to convert celsius to fahrenheit

def main():
    celsius = eval(input("what is the celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees fahrenheit")

main()
