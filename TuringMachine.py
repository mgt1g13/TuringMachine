from Checker import Checker

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
		self.__set_tape(input_tape)

		

		while self.current_state != self.final_state:
			executed = 0


			execution_threads = __set_transition_threads(executed)

			for thread in execution_threads:
				thread.join()

			if executed == False:
				break

		self._generate_output()

	def __set_transition_threads(self, executed):
		#sets a threads for each possible transition
		i = 0
		execution_threads = []
		for transition in self.states_transitions[self.current_state]:
			execution_threads.append(Checker(executed, self.tapes[i], transition))
			executed = execution_threads[i].start()
			i += 1
		return execution_threads


	def __set_tape(self, input_tape):
		#resets the current tapes and set the new input ready to use
		self.__reset_tapes()
		for symbol in input_tape:
			self.tapes[0].write(symbol)
			self.tapes[0].move_head_up()
		self.tapes[0].head = 0



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

	def __reset_tapes(self):
		self.tapes = []
		for i in range(n_tapes):
			self.tapes += [Tape(blank_char = self.tape_alphabet[len(self.tape)-1])]
