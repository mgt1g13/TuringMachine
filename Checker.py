from threading import Thread, Lock
from Executor import Executor

class  Checker(Thread):
	def __init__(self, executed, mt, transition):
		Thread.__init__(self)
		self.executed = executed
		self.mt = mt
		self.transition = transition

	def run(self):
		#Optmization check. Can suffer from race conditions, but it is going to be checked again 
		# on mutual exclusion
		if self.executed.integer == 1:
			return #False

		ok = self._check_transition()
		if(not ok):
			return #False

		# lock
		self.mt.mutex.acquire()

		# ok = self._check_transition()
		# if(not ok):
		# 	self.mt.mutex.release()
		# 	return #False

		
		if(self.executed.integer == 0):
			self.executed.integer = 1
		else:
			self.mt.mutex.release()
			return# False

		self.mt.mutex.release()

		
		#gera threads de execucao
		#join nas threads de exec
		exec_threads = self.__set_exec_threads()
		for thread in exec_threads:
			thread.join()
		
		self.executed.integer = 1

		
		self.mt.set_state(self.transition.post_state)
		# return True

	def _check_transition(self):
		#check all the pre conditions for a match, if theres any unmatching condition returns False
		for i in range(len(self.mt.tapes)):
			if self.transition.pre_conditions[i] != self.mt.tapes[i].read():
				return False
		return True

	def __set_exec_threads(self):
		#sets a threads for each tape
		exec_threads = []
		for i in range(len(self.mt.tapes)):
			exec_threads.append(Executor(self.mt.tapes[i], self.transition.post_conditions[i], self.transition.movements[i]))
			exec_threads[i].start()

		return exec_threads