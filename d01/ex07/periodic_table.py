import sys

def writeLine(str, f):
	f.write(str)
	f.flush()

def writeItem(f, i):
	writeLine("\t\t\t\t<td style=\"border: 1px solid black; padding:10px\">\n", f)
	writeLine("\t\t\t\t\t<h4>" + str(i[0].get('name')) + "</h4>\n", f)
	writeLine("\t\t\t\t\t<ul>\n", f)
	writeLine("\t\t\t\t\t\t<li>" + str(i[2].get('number')) + "</li>\n", f)
	writeLine("\t\t\t\t\t\t<li>" + str(i[3].get('small')) + "</li>\n", f)
	writeLine("\t\t\t\t\t\t<li>" + str(i[4].get('molar')) + "</li>\n", f)
	writeLine("\t\t\t\t\t\t<li>" + str(i[5].get('electron')) + " electron</li>\n", f)
	writeLine("\t\t\t\t\t</ul>\n", f)
	writeLine("\t\t\t\t</td>\n", f)

def writeEmptyItem(f):
	writeLine("\t\t\t\t<td style=\"border: 1px solid black; padding:10px\"> </td>\n", f)

def createHTML(items):
	# print(items.get("Hydrogen"))
	f = open('periodic_table.html', 'w')
	writeLine("<!DOCTYPE html>\n", f)
	writeLine("<html>\n", f)
	writeLine("\t<head>\n", f)
	writeLine("\t\t<title> Periodic table of the elements </title>\n", f)
	writeLine("\t\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n", f)
	writeLine("\t</head>\n", f)
	writeLine("\t<body>\n", f)
	writeLine("\t\t<table>\n", f)
	writeLine("\t\t\t<tr>\n", f)
	i = 0
	for item in items:
		if (i < len(items) - 1):
			futureItem = items[i + 1]
		if (item[1].get('position') == 17):
			writeItem(f, item)
			writeLine("\t\t\t</tr>\n", f)
			writeLine("\t\t\t<tr>\n", f)
			i = i + 1
			continue
		writeItem(f, item)
		if futureItem[1].get('position') != (item[1].get('position') + 1) and item[1].get('position') != 17:
			for tmp in range(item[1].get('position'), futureItem[1].get('position') - 1):
				writeEmptyItem(f)
		i = i + 1
			

	writeLine("\t\t</table>\n", f)
	writeLine("\t</body>\n", f)
	writeLine("</html>", f)
	# for i in items:
	f.close()

	


def parseLine(line, listItems):
	lineContent = line.split(',')
	item = lineContent[0].split('=') 
	itemName = item[0].strip()
	# itemPosition = item[1].replace('position:', '').strip()
	itemPosition = item[1].split(':')
	itemNumber = lineContent[1].split(':')
	itemSmall = lineContent[2].split(':')
	itemMolar = lineContent[3].split(':')
	itemElectron = lineContent[4].split(':')

	# itemNumber =  lineContent[1].replace('number:', '').strip()
	# itemSmall = lineContent[2].replace('small:', '').strip()
	# itemMolar = lineContent[3].replace('molar:', '').strip()
	# itemElectron = lineContent[4].replace('electron:', '').strip()
	properties = ({"name" : itemName}, {itemPosition[0].strip() : int(itemPosition[1].strip())}, {itemNumber[0].strip() : itemNumber[1].strip()}, 
					{itemSmall[0].strip() : itemSmall[1].strip()}, {itemMolar[0].strip() : itemMolar[1].strip()}, 
					{itemElectron[0].strip() : itemElectron[1].strip()})
	# dictItems.setdefault(itemName, properties);
	listItems.append(properties);

def compare(item):
	tmp = item[1]
	return tmp[1].get('position')

def parseContent(file):
	f = open(file, 'r')
	listItems = []
	inputContent = f.read().split('\n')
	for line in inputContent:
		# print(line)
		if len(line) > 0:
			parseLine(line, listItems)
	# print(listItems)
	createHTML(listItems)
	# print(sortedItems)
	# for number in result:
	# 	if number != 100:
	# 		print(number)
	f.close()


if __name__ == '__main__':
	if len (sys.argv) < 2:
		parseContent("periodic_table.txt")
	elif len (sys.argv) == 2:
		parseContent(sys.argv[1])
	else:
		exit(1)