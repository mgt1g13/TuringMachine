from threading import Thread

class  Executor(Thread):
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
		if(executed == 0):
			executed = 1
		else:
			return False

		#self._execute_transition()

	def _check_transition(self):
		for i in range(len(self.tapes)):
			print (self.tapes[i].read())
			print("Aqui ", self.transition.pre_condition[i])
			# if self.transition.pre_condition[i] != tapes[i]:
			# 	return False