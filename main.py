
from Parser import Parser
from TuringMachine import TuringMachine

parser = Parser()
parser.parse()


# parser, n_tapes, states, input_alphabet, tape_alphabet, initial_state, states_transitions, final_state, tm_type):
mt = TuringMachine(parser.n_tapes, parser.states, parser.input_alphabet, 
	parser.machine_alphabet, parser.states[0] ,parser.transitions, 
	parser.states[len(parser.states)-1], parser.tm_type)

tape_input = parser.get_input()
while tape_input != False:
	print("A" + str(parser.machine_alphabet))
	#print("Aqui" + str(tape_input[1]))
	mt.run(tape_input)
	tape_input = parser.get_input()

