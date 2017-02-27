import math
import re

def BMICalc(usrWeight, usrHeight):
	try:
		return ((float(usrWeight) / (float(usrHeight)**2)) * 703)
	except:
		return 0

def retCalc(usrAge, usrSal, usrSav, savGoal):
	try:
		return int(usrAge + math.floor(savGoal / (usrSal * (usrSav / 100))))
	except:
		return 0

def distCalc(x1, x2, y1, y2):
	try:
		return (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))
	except:
		return 0

def emailVerify(usrEmail):
	return bool(re.match("\w\w*@\w\w*\.[a-zA-Z]{3}$", str(usrEmail)))