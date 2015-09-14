class Tape:

	def __init__(self, tape=[], blankChar = ' '):
		#sequência de carateres para a tape
		if(tape == []):
			self.tape = [blankChar]
		else:
			self.tape = tape + [blankChar]
		#ponteiro para aonde está a cabeça
		self.head = 0
		#define caracter Branco
		self.blankChar = blankChar

	
	def write(self, char):
		self.tape[head] = char

	def read(self):
		return self.tape[cabeca]
	
	def moveHeadUp(self):
		self.head += 1
		if self.head == len(self.tape):
			self.tape += [self.blankChar]

	def moveHeadDown(self):
		if self.head > 0:
			self.head -= 1


