import re
from sys import stdin
from Transition import Transition

class Parser:
	

	def __strToSingleTapeTransition(self, string):
		return re.match( '\((.*),(.*)\)=\((.*),(.*),(.*)\)', string).groups()


	def __strToMultitapeTransition(self, line):
		tapeTransitions = line[:len(line)-1].split('|')
		transitions = list(map(self.__strToSingleTapeTransition, tapeTransitions))
		# [('q7', '1', 'q7', '1', 'E')]
		
		preState = ""
		postState = ""
		preConditions = []
		postConditions = []
		movements = []

		for i in range(0, len(tapeTransitions)):
			(preState, preCondition, postState, postCondition, movement) = transitions[0]
			postConditions += [postCondition]
			preConditions += [preCondition]
			movements += [movement]

		return Transition(preState,preConditions, postState,postConditions, movements)



	def parse(self):
		#Gets the number of tapes
		self.nTapes = int(stdin.readline())

		#gets the aux values
		line = stdin.readline()
		self.auxValues = list(map(int, line[:len(line)-1].split(' ')))
		print(self.auxValues)
		
		#get the states
		line = stdin.readline()
		self.states =  line[:len(line)-1].split(' ')
		print(self.states)

		#get the input Alphabet
		line = stdin.readline()
		self.inputAlphabet =  line[:len(line)-1].split(' ')
		print(self.inputAlphabet)

		#Get the machine Alphabet
		line = stdin.readline()
		self.machineAlphabet =  line[:len(line)-1].split(' ')
		print(self.machineAlphabet)



		self.transitions = dict()
		for i in range(self.auxValues[3]):
			line = stdin.readline()	
			transition = self.__strToMultitapeTransition(line)	
			if(transition.preState in self.transitions):
				self.transitions[transition.preState] += [transition]
			else:
				self.transitions[transition.preState] = [transition]
		
		
		print(self.transitions)





parser = Parser()
parser.parse()
print(parser.nTapes)


