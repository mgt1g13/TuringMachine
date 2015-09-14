class Tape:

	def __init__(self, tape=[], blank_char = ' '):
		#sequência de carateres para a tape
	    self.tape = [blank_char]
		#ponteiro para aonde está a cabeça
		self.head = 0
		#define caracter Branco
		self.blankChar = blank_char

	
	def write(self, char):
		self.tape[self.head] = char

	def read(self):
		return self.tape[self.head]
	
	def moveHeadUp(self):
		self.head += 1
		if self.head == len(self.tape):
			self.tape += [self.blank_char]

	def moveHeadDown(self):
		if self.head > 0:
			self.head -= 1


