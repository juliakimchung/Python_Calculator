import re
print("My Magical Calculator")
print("Type 'quit' to exit")

previous = 0
run = True

def performMath():
    global previous
    global run
    equation = input("Enter equation")
    if equation == 'quit':
        run = False
    else:
        previous = eval(equation)
        print("You typed ", previous)


while run:
    performMath()