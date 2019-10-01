Sum = 0

##MATHEMATICAL_FUNCTIONS##

#clear
def clear_Sum():
    global Sum
    Sum == 0

#add
def add_Sum (number):
    global Sum
    Sum = Sum + number

#sub
def sub_Sum (number):
    global Sum
    Sum = Sum - number

#multiply
def multi_Sum (number):
    global Sum
    Sum = Sum * number

#divied
def div_Sum (number):
    global Sum
    Sum = Sum / number
##########################

#Application Start:

print ("Welcome to Calcurenator")

a = int (input("What's the first number: "))
Sum = a

print ("What function would you like to run?\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
choice = int (input())
#switch statement for what function to run
switch = {
        1: add_Sum,
        2: sub_Sum,
        3: multi_Sum,
        4: div_Sum
    }

func = switch.get(choice)

b = int (input("What's the seccond number: "))

func(b)

print (Sum)
#GUI TIME
