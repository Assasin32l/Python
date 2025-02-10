from math import *


def tokenisation(term):
    tokenTerm = []
    i = 0

    while i < len(term):
        token = ""

        if term[i] in "1234567890.,":
            for j in range(i, len(term)):
                if term[j] in "1234567890.,":
                    token += term[j]
                
                else:
                    i = j
                    break
            
            else:
                i = len(term)

        elif term[i] == '-' and (i == 0 or term[i-1] in "+-*/^("):
            token = '-'
            i += 1

            if i < len(term) and term[i] in "1234567890.,":
                for j in range(i, len(term)):
                    if term[j] in "1234567890.,":
                        token += term[j]
                    
                    else:
                        i = j
                        break
                
                else:
                    i = len(term)

        elif term[i] in "+*/^()e":
            token = term[i]
            i += 1

        elif term[i:i+2] in ["pi"]:
            token = term[i:i+2]
            i += 2

        elif term[i:i+3] in ["sin", "cos", "tan"]:
            token = term[i:i+3]
            i += 3

        elif term[i:i+4] in ["sqrt", "asin", "acos", "atan"]:
            token = term[i:i+4]
            i += 4

        else:
            token = term[i]
            i += 1

        tokenTerm.append(token)

    return tokenTerm


def checkTerm(tokenTerm):
    for i in range(len(tokenTerm)):
        if tokenTerm[i] in "+-*/^":
            if i == 0 or i == len(tokenTerm) - 1:
                return False

            elif tokenTerm[i-1] in "+-*/^(" or tokenTerm[i-1] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan"]:
                return False

            elif tokenTerm[i+1] in "+-*/^)":
                return False

        elif tokenTerm[i] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan"]:
            if i == len(tokenTerm) - 1:
                return False

            elif tokenTerm[i+1] in "+-*/^)":
                return False

        elif tokenTerm[i] == "(":
            if i < len(tokenTerm) - 1 and tokenTerm[i+1] in "+*/^)":
                return False

        elif tokenTerm[i] == ")":
            if i > 0 and tokenTerm[i-1] in "+-*/^(":
                return False

    return True


def postfix(tokenisation):
    postfixTerm = []
    stack = []

    for i in range(len(tokenisation)):
        if tokenisation[i][0] in "1234567890.," or (tokenisation[i][0] == '-' and len(tokenisation[i]) > 1):
            postfixTerm.append(tokenisation[i])

        elif tokenisation[i] in ["e", "pi"]:
            postfixTerm.append(tokenisation[i])

        elif tokenisation[i] in "+-":
            while stack and (stack[-1] in "+-*/^" or stack[-1] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan"]):
                postfixTerm.append(stack.pop())

            stack.append(tokenisation[i])

        elif tokenisation[i] in "*/":
            while stack and (stack[-1] in "*/^" or stack[-1] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan"]):
                postfixTerm.append(stack.pop())

            stack.append(tokenisation[i])

        elif tokenisation[i] == "^":
            while stack and (stack[-1] == "^" or stack[-1] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan"]):
                postfixTerm.append(stack.pop())

            stack.append(tokenisation[i])

        elif tokenisation[i] in ["sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "("]:
            stack.append(tokenisation[i])

        elif tokenisation[i] == ")":
            while stack and stack[-1] != "(":
                postfixTerm.append(stack.pop())

            stack.pop()

    while stack:
        postfixTerm.append(stack.pop())

    return postfixTerm

def evaluation(postfixTerm):
    stack = []

    for i in range(len(postfixTerm)):
        if postfixTerm[i][0] in "1234567890.," or (postfixTerm[i][0] == '-' and len(postfixTerm[i]) > 1):
            stack.append(float(postfixTerm[i]))

        elif postfixTerm[i] == "e":
            stack.append(e)

        elif postfixTerm[i] == "pi":
            stack.append(pi)

        elif postfixTerm[i] == "+":
            stack.append(stack.pop() + stack.pop())

        elif postfixTerm[i] == "-":
            stack.append(-stack.pop() + stack.pop())

        elif postfixTerm[i] == "*":
            stack.append(stack.pop() * stack.pop())

        elif postfixTerm[i] == "/":
            stack.append((1 / stack.pop()) * stack.pop())

        elif postfixTerm[i] == "^":
            x = stack.pop()
            stack.append(stack.pop() ** x)

        elif postfixTerm[i] == "sqrt":
            stack.append(sqrt(stack.pop()))

        elif postfixTerm[i] == "sin":
            stack.append(sin(stack.pop()))

        elif postfixTerm[i] == "cos":
            stack.append(cos(stack.pop()))

        elif postfixTerm[i] == "tan":
            stack.append(tan(stack.pop()))

        elif postfixTerm[i] == "asin":
            stack.append(asin(stack.pop()))

        elif postfixTerm[i] == "acos":
            stack.append(acos(stack.pop()))

        elif postfixTerm[i] == "atan":
            stack.append(atan(stack.pop()))

    result = stack.pop()

    return result


def tutorial():
    print("\nFor the Numbers, you can use either . or , as the decimal point.")
    print("For the Negative Numbers, you can use either - or (-).")
    print("Operators and Functions: +, -, *, /, ^, sqrt(), sin(), cos(), tan(), asin(), acos(), atan().")
    print("For Constants, you can use: e, pi.")
    print("You can also use ( and ).")
    print("\nExample: 2 + (-3) * 4 / (5 - 1) ^ 2")
    print("Example: sqrt(4) + sin(pi / (-2))")
    print("\nHave fun!")


print("\nHello, user. This is a calculator.\n\nAre you sure that whatever you are doing is worth it?")
uselessQuestions1 = input("Yes / No: ")
print("\nAnyway, let's start with the tutorial.")


print("\nFirst of all, do you want to skip the tutorial?")
uselessQuestions2 = input("Yes / No: ").lower()

if uselessQuestions2 in ["yes", "y"]:
    print("\nAre you sure? This is a very useful tutorial.")
    uselessQuestions3 = input("Yes / No: ").lower()

    if uselessQuestions3 in ["yes", "y"]:
        print("\nHmm. I think you missed the keys on the keyboard. Let's try again.")
        uselessQuestions4 = input("Yes / No: ").lower()

        if uselessQuestions4 in ["yes", "y"]:
            print("\nYou are not very good at this, are you? I make it easier for you.")
            uselessQuestions5 = input("Yes / Yes: ").lower()

            print("\nThere you go. Now we can start.")

        elif uselessQuestions4 in ["no", "n"]:
            print("\nYou don´t want to try again? I think you should. I will even make it easier for you.")
            uselessQuestions5 = input("Yes / Yes: ").lower()

            print("\nGood. Let's start the tutorial.")

    elif uselessQuestions3 in ["no", "n"]:
        print("\nGood. Let's start the tutorial.")

elif uselessQuestions2 in ["no", "n"]:
    print("\nGood. Let's start the tutorial.")

tutorial()


history = ["","","","","","","","","",""]

while True:
    print("\nMain menu: ")
    print("1. Calculate (c)")
    print("2. History (h)")
    print("3. Tutorial (t)")
    print("4. Quit (q)")

    choice = input("\nSelect one of the options: ").lower()

    while choice not in ["c", "calculate", "h", "history", "t", "tutorial", "q", "quit"]:
        print("\nInvalid choice. Please try again.")
        print("1. Calculate (c)")
        print("2. History (h)")
        print("3. Tutorial (t)")
        print("4. Quit (q)")

        choice = input("\nSelect one of the options: ").lower()

    if choice in ["c", "calculate"]:
        while True:
            term = input("\nPlease enter the term to be calculated: ")

            cleanTerm = term.replace(" ", "").lower()

            if cleanTerm != "":
                tokenTerm = tokenisation(cleanTerm)
                
                if not checkTerm(tokenTerm):
                    print("\nInvalid term. Please try again.")
                    continue

                postfixTerm = postfix(tokenTerm)
                result = round(evaluation(postfixTerm), 2)

                print("\nThe result of", term, "is", result)

                history.pop(0)
                history.append(term + " = " + str(result))

                break

            else:
                print("\nInvalid term. Please try again.")

    elif choice in ["h", "history"]:
        print("\nHistory: ")

        if history[9] != "":
            for i in range(10):
                if history[i] != "":
                    print(history[i])
        
        else:
            print("No history yet.")
    
    elif choice in ["t", "tutorial"]:
        tutorial()
    
    elif choice in ["q", "quit"]:
        break