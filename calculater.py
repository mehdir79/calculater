def calc (first,second,operator):

    if(operator == "*"):
        return first * second
    elif(operator == "+"):
        return first + second
    elif(operator == "-"):
        return first - second
    elif(operator == "/"):
        try:
            return first/second 
        except ZeroDivisionError:
            print("second should be not zero")
            return "try again"
    else:
        print("invalid operator")
        return
while(True):
    print("enter ur first num:")
    try:
        num1 = float(input())
    except:
        print("enter number not chars")
        continue
    print("enter ur second num:")
    try:
        num2 = float(input())
    except:
        print("enter number not chars")
        continue
    print("enter ur operator:")
    operator = input()

    print(calc(num1 , num2 , operator))