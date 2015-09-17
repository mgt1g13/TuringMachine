class Tape:

	def __init__(self, tape=[], blank_char = ' '):
		#sequencia de carateres para a tape
		self.tape = [blank_char]
		#ponteiro para aonde esta a cabeca
		self.head = 0
		#define caracter Branco
		self.blank_char = blank_char

	
	def write(self, char):
		self.tape[self.head] = char

	def read(self):
		return self.tape[self.head]
	
	def move_head_up(self):
		self.head += 1
		if self.head == len(self.tape):
			self.tape += [self.blank_char]

	def move_head_down(self):
		if self.head > 0:
			self.head -= 1


