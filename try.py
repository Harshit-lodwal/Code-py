
def summation():
    a=int(input("ENTER FIRST NUMBER:"))
    b=int(input("ENTER SECOND NUMBER:"))
    c=a+b
    print("SUMMATION OF TWO NUMBERS IS:",c)
def reminder():
    a=int(input("ENTER FIRST NUMBER:"))
    b=int(input("ENTER SECOND NUMBER:"))
    c=a%b
    print("REMINDER OF TWO NUMBERS IS:",c)
def type_finding():
    a=input("ENTER ANYTHING:")
    print("TYPE OF ENTERED VALUE IS:",type(a))
def comparision():
    a=int(input("ENTER FIRST NUMBER:"))
    b=int(input("ENTER SECOND NUMBER:"))
    if a>b:
        print(a,"IS GREATER THAN",b)
    elif a<b:
        print(b,"IS GREATER THAN",a)
    else:
        print("BOTH ARE EQUAL")
def average():
    a=int(input("ENTER FIRST NUMBER:"))
    b=int(input("ENTER SECOND NUMBER:"))
    c=int(input("ENTER THIRD NUMBER:"))
    d=(a+b+c)/3
    print("AVERAGE OF THREE NUMBERS IS:",d)     
def squaring():
    a=int(input("ENTER A NUMBER:"))
    b=a*a
    print("SQUARING OF A NUMBER IS:",b)
n="y"
while n=="y":
    number=int(input("""PRESS [1] TO PERFORM SUMMATION OPERATION
PRESS [2] TO PERFORM REMINDER FINDING OPERATION
PRESS [3] TO PERFORM TYPE FINDING OPERATION
PRESS [4] TO PERFORM COMPARISION OPERATION
PRESS [5] TO PERFORM AVERAGE OPERATION
PRESS [6] TO PERFORM SQUARING OPERATION
PRESS [7] TO PERFORM END OPERATIONS:"""))
    if number==1:
        summation()
    elif number==2:
        reminder()
    elif number==3:
        type_finding()
    elif number==4:
        comparision()
    elif number==5:
        average()
    elif number==6:
        squaring()
    elif number==7:
        break
    else:
        print("INVALID INPUT")
    n=input("DO YOU WANT TO PERFORM ANOTHER OPERATION? (y/n):")