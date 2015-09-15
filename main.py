
from Parser import Parser
from TuringMachine import TuringMachine

parser = Parser()
parser.parse()


# parser, n_tapes, states, input_alphabet, tape_alphabet, initial_state, states_transitions, final_state, tm_type):
mt = TuringMachine(parser.nTapes, parser.states, parser.inputAlphabet, 
	parser.machineAlphabet, parser.states[0] ,parser.transitions, 
	parser.states[len(parser.states[0])-1], parser.TMType)