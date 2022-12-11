import sys


def numbers_print():
	f = open("numbers.txt", 'r')
	result = f.read().split(',')
	for number in result:
		if number != 100:
			print(number)
	f.close()


if __name__ == '__main__':
	numbers_print()