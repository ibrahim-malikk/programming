#avg2.py
# A simple program to average two exam scores

def main():
    print("This program computes the average of two exam scores")

    score1, score2 = eval(input("Enter two scores seperated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the score is:", average)

main()
