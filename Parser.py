import re
from sys import stdin
from Transition import Transition

class Parser:
	

	def __str_to_single_tape_transition(self, string):
		#print(string)
		return re.match( '\((.*),(.*)\)=\((.*),(.*),(.*)\)', string).groups()


	def __str_to_multi_tape_transition(self, line):
		tape_transitions = line[:len(line)-1].split('|')
		transitions = list(map(self.__str_to_single_tape_transition, tape_transitions))
	

		
		pre_state = ""
		post_state = ""
		pre_conditions = []
		post_conditions = []
		movements = []

		for i in range(0, len(tape_transitions)):
			(pre_state, pre_condition, post_state, post_condition, movement) = transitions[i]
			post_conditions += [post_condition]
			pre_conditions += [pre_condition]
			movements += [movement]

		# print( pre_state + ": " + str(pre_conditions))
		return Transition(pre_state,pre_conditions, post_state,post_conditions, movements)



	def parse(self):
		#Gets the number of tapes
		self.n_tapes = int(stdin.readline())

		#gets the aux values
		line = stdin.readline()
		print(line[:len(line)-1].split(' '))
		self.aux_values = list(map(int, line[:len(line)-1].split(' ')))
		# print(self.aux_values)
		
		#get the states
		line = stdin.readline()
		self.states =  line[:len(line)-1].split(' ')
		# print(self.states)

		#get the input Alphabet
		line = stdin.readline()
		self.input_alphabet =  line[:len(line)-1].split(' ')
		# print(self.input_alphabet)

		#Get the machine Alphabet
		line = stdin.readline()
		self.machine_alphabet =  line[:len(line)-1].split(' ')
		# print(self.machine_alphabet)



		self.transitions = dict()
		for i in range(self.aux_values[3]):
			line = stdin.readline()	
			transition = self.__str_to_multi_tape_transition(line)	
			if(transition.pre_state in self.transitions):
				self.transitions[transition.pre_state] += [transition]
			else:
				self.transitions[transition.pre_state] = [transition]

		# print(self.transitions)
		
		#Reads the Turing machine type
		line = stdin.readline()	
		self.tm_type = line[:len(line)-1]
		# print(self.tm_type)

		#reads the number of inputs
		line = stdin.readline()
		self.number_inputs = int(line[:len(line)-1])

		self.inputs = []
		for i in range(self.number_inputs):
			line = stdin.readline()
			self.inputs += [line[:len(line)-1]]

		# print(self.inputs)
		self.next_input = 0
	

	def get_input(self):
		#returns the next input tape, if theres one. else it returns False
		if self.next_input == self.number_inputs:
			return False
		self.next_input += 1
		return self.inputs[self.next_input - 1]




# parser = Parser()
# parser.parse()
# print(parser.n_tapes)


