from eqvSolver import *
from tokenization import *
from validation import *
from calculation import *

def reduceExpr(tokens):
	degree = 0
	for token in tokens:
		if (token.pwr > degree):
			degree = token.pwr
	if (degree > 2):
		print("Polynomial degree is too big. Exiting...")
		exit (3)
	reducedExpr = [None] * 3
	for token in tokens:
		if (not reducedExpr[2 - int(token.pwr)]):
			reducedExpr[2 - int(token.pwr)] = token.mult * token.neg
		else:
			reducedExpr[2 - int(token.pwr)] = reducedExpr[2 - int(token.pwr)] + (token.mult * token.neg)
	i = 0
	while (i < 3):
		if (reducedExpr[i] == None):
			reducedExpr[i] = 0.0
		i += 1
	return (reducedExpr)

def printRedForm(redExpr):
	out = "Reduced form: "
	if (redExpr[0] != 0):
		out += str(redExpr[0])
		out += " * X^2 "
	if (redExpr[1] != 0):
		if (redExpr[0] == 0):
			out += str(redExpr[1])
		elif (redExpr[1] < 0):
			out += "- "
			out += str(-redExpr[1])
		else:
			out += "+ "
			out += str(redExpr[1])
		out += " * X "
	if (redExpr[2] != 0):
		if (redExpr[0] != 0 or redExpr[1] != 0):
			if (redExpr[2] < 0):
				out += "- "
				out += str(-redExpr[2])
			else:
				out += "+ "
				out += str(redExpr[2])
			out += " "
	out += "= 0"
	print(out)
	haveFirst = haveSecond = haveZero = False
	degree = None
	if (redExpr[0] != 0):
		haveSecond = True
		degree = 2
	if (redExpr[1] != 0):
		haveFirst = True
		if (degree == None):
			degree = 1
	if (redExpr[2] != 0):
		haveZero = True
		if (degree == None):
			degree = 0
	print("Polinomial degree is: " + str(degree))
	pickOpt(redExpr[0], redExpr[1], redExpr[2], haveFirst, haveSecond, haveZero)
	return