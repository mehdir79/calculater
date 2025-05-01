while(True):
    print("enter ur first num:")
    try:
        first = float(input())
    except:
        print("enter number not chars")
        continue
    print("enter ur second num:")
    try:
        second = float(input())
    except:
        print("enter number not chars")
        continue
    print("enter ur operator:")
    operator = input()
    if(isinstance(first , float or int) == False or isinstance(second , float or int) == False):
        print("wrong inputs try again")
        continue

    def calc (first,second,operator):
    
        if operator in [("+") , ("-") , ("/") , ("*")]:
            if(operator == "*"):
                return first * second
            elif(operator == "+"):
                return first + second
            elif(operator == "-"):
                return first - second
            elif(operator == "/"):
                try:
                    first/second == ZeroDivisionError
                except:
                    #raise ZeroDivisionError("secound should be not zero")
                    print("secound should be not zero")
                    return "try again"
                else:
                    return first / second
            else:
                print("wrong nums")
                return
        else: 
            print("wrong operators") 
            return                 
    print(calc(first , second , operator))