name = "rahul"

while True:
    print("rahul")
    print("find letters in word")
    
    num = int(input("enter number: "))

    if num == len(name):
        print("congratulation")
        break

    elif num < len(name):

        print("think bigger number")
    
    elif num > len(name):
        print("think smaller number")
