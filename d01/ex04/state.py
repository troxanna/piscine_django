import sys

def printState(capitalCity, resultDict):
	if capitalCity in resultDict:
		print(resultDict[capitalCity])
	else:
		print("Unknown capital city")

def joinDict(capitalCity):
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
				resultDict.setdefault(capital_cities[c], s);
	printState(capitalCity, resultDict);


	

if __name__ == '__main__':
	if len (sys.argv) != 2:
		exit(1);
	else:
		joinDict(sys.argv[1])