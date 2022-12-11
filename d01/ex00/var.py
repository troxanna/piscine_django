def	my_var():
	varInt = 42;
	varFloat = 42.0;
	varStrFirst = "42";
	varStrSecond = "quarante-deux";
	varBool = True;
	varList = [42];
	varDict = {42:42};
	varTuple = (42, );
	varSet = set();
	print(varInt, "has a type", type(varInt))
	print(varStrFirst, "has a type", type(varStrFirst))
	print(varStrSecond, "has a type", type(varStrSecond))
	print(varFloat, "has a type", type(varFloat))
	print(varBool, "has a type", type(varBool))
	print(varList, "has a type", type(varList))
	print(varDict, "has a type", type(varDict))
	print(varTuple, "has a type", type(varTuple))
	print(varSet, "has a type", type(varSet))


if __name__ == '__main__':
	my_var();