import re
from validation import *
from tokenization import *
from simplification import *
from calculation import *

class Token:
    def __init__(self, name):
        self.neg = 0
        self.name = name
        self.pwr = 0
        self.mult = 1
    def addPower(self, pwr):
        self.pwr = pwr
    def addMult(self, mult):
        self.mult = mult
    def makeNeg(self, i):
        self.neg = i
    def printToken(self):
        if (self.neg == 1):
            print("(" + self.name + "^" + str(self.pwr) + " * " + str(self.mult) + ")")
        else:
            print("-(" + self.name + "^" + str(self.pwr) + " * " + str(self.mult) + ")")

if __name__ == '__main__':
    def isPriotityEqualOrLess(op1, op2):
        if (op1 == "+" or op1 == "-"):
            prior1 = 1;
        else:
            prior1 = 2;
        if (op2 == "+" or op2 == "-"):
            prior2 = 1;
        else:
            prior2 = 2;
        return (prior1 - prior2)

    def makeRPN(expr):
        operations = '+', '-', '*', '/'
        tokens = expr
        stack = []
        ret = []
        for token in tokens:
            if (operations.__contains__(token)):
                while (len(stack) != 0 and operations.__contains__(stack[-1]) == True):
                    if (isPriotityEqualOrLess(token, (stack[0])) <= 0):
                        ret.append(stack.pop())
                        continue
                    break
                stack.append(token)
            elif (token == '('):
                stack.append(token)
            elif (token == ')'):
                while (stack and stack[-1] != '('):
                    ret.append(stack.pop())
                stack.pop()
            elif (token == ''):
                continue
            else:
                ret.append(token)
        while (stack):
            ret.append(stack.pop())
        return (ret);

    def makeTokens(rpnExpr, var):
        tokens = []
        shouldBeNeg = 1
        haveToken = False
        haveMult = False
        for elem in rpnExpr:
            if (elem== ''):
                continue
            if (elem.__contains__(varname) == True):
                token = Token(varname)
                token.addPower(processNumber(elem, elem.index('^') + 1))
                haveToken = True
            elif (elem.isdigit() == True):
                mult = float(elem)
                haveMult = True
            # elif (elem == '*'):
            #     token.addMult(mult)
            elif (elem == '+' or elem == "-"):
                token.makeNeg(shouldBeNeg)
                if (elem == '-'):
                    shouldBeNeg = -1;
                else:
                    shouldBeNeg = 1
            if (haveMult == True and haveToken == True and shouldBeNeg != 0):
                token.addMult(mult)
                token.makeNeg(shouldBeNeg)
                shouldBeNeg = 0
                haveToken = False
                haveMult = False
                tokens.append(token)
        for token in tokens:
            token.printToken()
        return (tokens)


# Handle gaps in numbers!!!!
    expr = "X^2 = -5"
    varName = validateExpr(expr)
    tokens = parseForTokens(expr, varName)
    tokens = reduceExpr(tokens)
    printRedForm(tokens)
