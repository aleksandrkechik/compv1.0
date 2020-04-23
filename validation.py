from eqvSolver import *
from tokenization import *
from calculation import *

def validateExpr(expr):
	allowed = '+', '-', '=', '*', ' ', '^', '.'
	found = 0
	i = 0
	varName = None
	while (i < len(expr)):
		if (not allowed.__contains__(expr[i])):
			if (expr[i].isdigit()):
				i += 1
				continue
			else:
				if (found == 0):
					varName = expr[i]
					found = 1
				else:
					if (not expr[i] == varName):
						print("Invalid data!")
						exit(2)
		if (expr[i] == '^'):
			validatePower(expr, i)
		i += 1
	if (varName == None):
		print("The input can't be calculated. No variable found. Exiting...")
		exit (5)
	# additionalValidation(expr, varName)
	return (varName)

def additionalValidation(expr, varName):
	operators = '*', '+', '-'
	multStart = False
	varStart = False
	hadOperator = False
	digitsStart = False
	for i in expr:
		if (i.isdigit()):
			if (hadOperator):
				hadOperator = False
			if (not varStart):
				multStart = True
		else:
			digitsStart = False
		if (multStart and (i != ' ' or not operators.__contains__(i))):
			print("Invalid input. Exiting")
			exit(6)
		if (hadOperator and operators.__contains__(i)):
			print("Invalid input. Exiting")
			exit(6)
		if (operators.__contains__(i)):
			if (multStart):
				multStart = False
			if (varStart):
				varStart = False
			hadOperator = True
		if (i == varName):
			varStart = True