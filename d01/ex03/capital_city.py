import sys

def printCapitalCity(state, resultDict):
	if state in resultDict:
		print(resultDict[state])
	else:
		print("Unknown state")

def joinDict(state):
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
	printCapitalCity(state, resultDict);


	

if __name__ == '__main__':
	if len (sys.argv) != 2:
		exit(1);
	else:
		joinDict(sys.argv[1])