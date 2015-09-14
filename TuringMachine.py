class TuringMachine:

	def __init__(self, n_tapes, states, input_alphabet, tape_alphabet, initial_state, states_transitions, final_state, tm_type):
		#sets basic information about the TM
		self.states = states
		self.input_alphabet = input_alphabet
		self.tape_alphabet = tape_alphabet
		
		#allocate the number of needed tapes
		self.n_tapes = n_tapes

		#sets current state as being the initial one
		self.current_state = initial_state
		
		self.states_transitions = states_transitions
		self.final_state = final_state
		
		#sets the turing machine type: language recognition or function processing
		self.tm_type = tm_type

	
	def run(self, input_tape):
		self._reset_tapes()
		self.tapes[0].tape = input_tape

		while self.current_state != self.final_state:
			executed = 0
			check_n_exec_transitions()
			#len(self.states_transitions[self.current_state] -> threads

			if executed == False:
				break

		self._generate_output()

	def _generate_output(self):
		#generates the output according to the machine type
		if self.tm_type == 	'R':
			if self.current_state == self.final_state:
				print("aceita")
			else:
				print("rejeita")

		else:
			if self.current_state == self.final_state:
				print("rejeita")
			else:
				print(self.tapes[0])

	def _reset_tapes(self):
		self.tapes = []
		for i in range(n_tapes):
			self.tapes += [Tape(blank_char = self.tape_alphabet[len(self.tape)-1])]