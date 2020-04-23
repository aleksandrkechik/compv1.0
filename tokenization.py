from eqvSolver import *
from validation import *
from calculation import *
from simplification import *

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

def skipNumber(expr, i):
	while (i < len(expr) and (expr[i].isdigit() == True or expr[i] == '.')):
		if (expr[i] == '.' and expr[i + 1].isdigit() != True):
			print("Invalid data!")
			exit(2)
		i += 1
	return i - 1

def parseForTokens(expr, varName):
	afterDigit = ' ', '+', '-', '=', '*'
	i = 0
	rightPart = False
	haveToken = False
	haveMult = False
	shouldBeNeg = 1
	tokens = []
	while (i < len(expr)):
		# if (expr[i] == '='):
		# 	rightPart = True
		# 	shouldBeNeg = -1
		if (expr[i].isdigit() == True):
			mult = processNumber(expr, i)
			haveMult = True
			if (haveToken == True):
				token.addMult(mult)
				haveMult = False
				haveToken = False
				tokens.append(token)
			i = skipNumber(expr, i)
			if (i < len(expr) - 1 and not afterDigit.__contains__(expr[i + 1])):
				print("Invalid data!")
				exit(2)
		# elif (expr[i] == '*'):
		elif (expr[i] == varName):
			token = handleVar(expr, i, varName)
			i = skipPwr(expr, i)
			token.makeNeg(shouldBeNeg)
			haveToken = True
			if (haveMult == True):
				token.addMult(mult)
				haveMult = False
				haveToken = False
				tokens.append(token)
		elif (expr[i] == '+' or expr[i] == '-' or expr[i] == '='):
			if (haveMult == True and haveToken == False):
				token = Token(varName)
				token.addMult(mult)
				token.addPower(0)
				token.makeNeg(shouldBeNeg)
				tokens.append(token)
				haveMult = False
			elif (haveMult == False and haveToken == True):
				tokens.append(token)
				haveToken = False
			if (expr[i] == '='):
				rightPart = True
				shouldBeNeg = -1
			if ((rightPart == False and expr[i] == '+') or (rightPart == True and expr[i] == '-')):
				shouldBeNeg = 1
			elif ((rightPart == False and expr[i] == '-') or (rightPart == True and expr[i] == '+')):
				shouldBeNeg = -1
		i += 1
	if (haveMult):
		token = Token(varName)
		token.makeNeg(shouldBeNeg)
		token.mult = mult
		token.pwr = 0
		tokens.append(token)
	# for token in tokens:
	# 	token.printToken()
	return (tokens)

def skipPwr(expr, i):
	if (i + 1 < len(expr)):
		if (expr[i + 1] == '^'):
			return (skipNumber(expr, i + 2))
		return (i)
	return (i)

def handleVar(expr, i, varname):
	token = Token(varname)
	if (i + 1 < len(expr) and expr[i + 1] == '^'):
		validatePower(expr, i + 1)
		token.addPower(processNumber(expr, i + 2))
	else:
		token.addPower(1)
	return (token)


def processNumber(expr, i):
	ret = 0
	extra = 0
	length = 0
	while (i < len(expr)):
		if (expr[i] == '.'):
			i += 1
			break
		if (expr[i].isdigit() == False):
			return (ret / 10);
		ret += int(expr[i])
		ret *= 10
		i += 1
	while (i < len(expr)):
		if (expr[i] == '.'):
			i += 1
			break
		if (expr[i].isdigit() == False):
			while (length >= 0):
				extra /= 10
				length -= 1
			return (ret / 10 + extra)
		extra += int(expr[i])
		extra *= 10
		length += 1
		i += 1
	return (ret / 10 + extra)


def validatePower(expr, i):
	if (not expr[i + 1].isdigit() and not (expr[i + 1] == '.' and expr[i + 2].isdigit())):
		print("Invalid data!")
	return