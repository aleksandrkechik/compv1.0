from eqvSolver import *
from tokenization import *
from validation import *

def pickOpt(a, b, c, haveFirst, haveSecond, hazeZero):
	answer = 0
	if (haveFirst and haveSecond):
		answer = solveBig(a, b, c)
	# elif (haveFirst and haveSecond and hazeZero):
	# 	print("")
	elif (haveFirst and hazeZero):
		solveSimple(b, c)
	elif (haveSecond and hazeZero):
		getSimpleSecond(a, c)
	elif (haveSecond or haveFirst):
		print("The solution is:")
		print("0")
	elif (hazeZero):
		if (first.mult != 0):
			print("Invalid data!")
			exit(4)
	# print("The solution is:")
	# print(answer)
	return

def getSimpleSecond(a, c):
	if (c > 0):
		print("Square root from negative number. Expression is unsolvable. Exiting...")
		exit(5)
	answer = getSqrt(-c/a)
	return (answer)

def getSqrt(num):
	limMax = num / 2
	limMin = 0.0
	while (limMin * limMin != num):
		limMax = (limMax + (num / limMax)) / 2
		if (limMin == limMax):
			break
		limMin = limMax
	return (limMin)

def solveBig(a, b, c):
	sqDis = b * b - 4 * a * c
	if (sqDis < 0):
		print("Discriminant is strictly negative, no solutions. Exiting...")
	elif (sqDis == 0):
		print("Discriminant equals 0, the solution is:")
		ret1 = (-b + discr) / 2 * a
		print(ret1)
	else:
		discr = getSqrt(sqDis)
		ret1 = (-b + discr) / 2 * a
		ret2 = (-b - discr) / 2 * a
		print("Discriminant is strictly positive, the two solutions are:")
		print(ret1)
		print(ret2)
	return

def solveSimple(b, c):
	answer = -c / b
	print("The solution is:")
	print(answer)
	return