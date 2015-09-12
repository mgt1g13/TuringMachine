

from sys import stdin

class Parser:
	

	def __strToInt(s):
		return int(s)

	def parse(self):
		#Gets the number of tapes
		line = stdin.readline()
		self.nTapes = int(line)

		#gets the aux values
		line = stdin.readline()
		self.auxValues = list(map(int, line[:len(line)-2].split(' ')))
		print(self.auxValues)
		



# parser = Parser()

# parser.parse()

# print(parser.nTapes)


