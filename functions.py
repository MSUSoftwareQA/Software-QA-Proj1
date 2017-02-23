import math
import re

def BMICalc(usrWeight, usrHeight):
	return ((usrWeight / (usrHeight**2)) * 703)

def retCalc(usrAge, usrSal, usrSav, savGoal):
	return int(usrAge + math.floor(savGoal / (usrSal * (usrSav / 100))))

def distCalc(x1, x2, y1, y2):
	return (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))

def emailVerify(usrEmail):
	return bool(re.match("\w\w*@\w\w*.[a-zA-Z]{3}$", usrEmail))