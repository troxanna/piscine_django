import sys

def printState(capitalCity, state):
	print("%s is the capital of %s"%(state, capitalCity))



def printCapitalCity(state, capitalCity):
	print("%s is the capital of %s"%(state, capitalCity))


def	printResult(resultArgs, resultDict):
	for arg in resultArgs:
		flag = 0
		for key, value in resultDict.items():
			if (key == arg or key.upper() == arg.upper()):
				printState(key, value)
				flag = 0
				break 
			elif (value == arg or value.upper() == arg.upper()):
				printCapitalCity(value, key)
				flag = 0
				break 
			else:
				flag = 1
		if flag == 1:
			print("%s is neither a capital city nor a state" %(arg))
				


def joinDict(resultArgs):
	resultDict = {}
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for s in states.keys():
		for c in capital_cities.keys():
			if (states[s] == c):
				resultDict.setdefault(s, capital_cities[c]);
	printResult(resultArgs, resultDict)


def parseArgs(args):
	resultArgs = []
	tmpArgs = args.split(",");
	for item in tmpArgs:
		if len(item.strip()) > 0:
			resultArgs.append(item.strip())
	joinDict(resultArgs)


if __name__ == '__main__':
	if len (sys.argv) != 2:
		exit(1);
	else:
		parseArgs(sys.argv[1])