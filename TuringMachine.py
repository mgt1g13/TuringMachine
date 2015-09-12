class TuringMachine:

	def __init__(self, nTapes, inputString, initialState, statesTransitions, finalState):
		#allocate the number of needed tapes
		self.nTapes = nTapes
		self.tapes = []
		for i in range(nTapes):
			self.tapes += [[]]
		#place the innput on tape 0
		self.tapes[0] = inputString
		#sets current state as being the initial one
		self.currentState = initialState
		
		self.statesTransitions = statesTransitions
		self.finalState = finalState

