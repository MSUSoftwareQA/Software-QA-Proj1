import pytest
import functions

def test_BMI():
	assert functions.BMICalc(100, 60) == 19.527777777777775
	assert functions.BMICalc(200, 90) == 17.358024691358025
	assert functions.BMICalc(12, 23) == 15.947069943289225
	with pytest.raises(TypeError):
		assert functions.BMICalc('a', 23) != 20

def test_Ret():
	assert functions.retCalc(20, 40000, 30, 50000) == 24
	assert functions.retCalc(5, 10, 100, 500) == 55
	assert functions.retCalc(99, 1000, 2, 500) == 124
	with pytest.raises(TypeError):
		assert functions.retCalc('a', 23,"g", 50) != 20

def test_Dist():
	assert functions.distCalc(5, 5, 10, 5) == 5
	assert functions.distCalc(1, 50, 120, 3) == 126.84636376341263
	assert functions.distCalc(9999, 12, 3, 45920) == 46990.54221862097
	with pytest.raises(TypeError):
		assert functions.distCalc('a', 23, 200,30) != 20
def test_Email():
	assert functions.emailVerify("alc552@msstate.edu") == True
	assert functions.emailVerify("$Asd%!@msstate.edu") == False
	assert functions.emailVerify("@.edu") == False
	assert functions.emailVerify("alc552.msstate@edu") == False
	assert functions.emailVerify("dddd@dddd") == False
