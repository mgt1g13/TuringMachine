class TuringMachine:

	def __init__(self, n_tapes, states, input_alphabet, tape_alphabet, initial_state, states_transitions, final_state, tm_type):
		#sets basic information about the TM
		self.states = states
		self.input_alphabet = input_alphabet
		self.tape_alphabet = tape_alphabet
		
		#allocate the number of needed tapes
		self.n_tapes = n_tapes
		self.tapes = []
		for i in range(n_tapes):
			self.tapes += [[]]
		#sets current state as being the initial one
		self.current_state = initial_state
		
		self.states_transitions = states_transitions
		self.final_state = final_state
		#sets the turing machine type: language recognition or function processing
		self.tm_type = tm_type

	
	def run(self, input_tape):
		self.tapes[0] = input_tape
		
		
		
		
