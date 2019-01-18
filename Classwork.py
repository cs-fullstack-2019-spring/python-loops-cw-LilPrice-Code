def main():
    # exer1()
    # exer2()
    # exer3()
    # exer4()
    Fuzz()



def exer1():
    i = -20
    while i <= 50:
        print(i)
        i+=1


def exer2():
    n = 0
    while n <=20:
        print(n)
        n += 2


def exer3():
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    num3 = int(input("Enter 3rd number "))
    ave = ((num1 + num2 + num3)/3)
    print("The average of",num1,num2,num3,"is",ave)


def exer4():
    password = input("Please enter your Password.")
    while True:
        password1 = input("Please Reenter you password")
        if password == password1:
            print("Thank You")
            break
        elif password1 == "q":
            print("User has Quit")
            break
        else:
            print("Try again")


def Fuzz():
    number = int(input("Please enter a number."))
    x = 0
    while x <= number:
        if x % 3 == 0 & x % 5 == 0:
            print("FIZZBUZZ")
            x += 1

        elif x % 3== 0:
            print("FIZZ")
            x +=1

        elif x % 5== 0:
            print("BUZZ")
            x += 1

        else:
            print(x)
            x += 1



if __name__ == '__main__':
    main()