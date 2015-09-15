from threading import Thread
from Executor import Executor

class  Checker(Thread):
	def __init__(self, executed, tapes, transition):
		self.executed = executed
		self.tapes = tapes
		self.transition = transition

	def run(self):
		if self.executed == 1:
			return False

		ok = self._check_transition()
		if(not ok):
			return False

		# lock
		if(self.executed == 0):
			self.executed = 1
		else:
			return False

		#gera threads de execucao
		#join nas threads de exec
		return True

	def _check_transition(self):
		#check all the pre conditions for a match, if theres any unmatching condition returns False
		for i in range(len(self.tapes)):
			print (self.tapes[i].read())
			print("Aqui ", self.transition.pre_condition[i])
			if self.transition.pre_condition[i] != tapes[i]:
				return False
		return True