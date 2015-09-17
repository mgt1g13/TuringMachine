from threading import Thread, Lock
from Executor import Executor

class  Checker(Thread):
	def __init__(self, executed, tapes, transition, mutex):
		Thread.__init__(self)
		self.executed = executed
		self.tapes = tapes
		self.transition = transition
		self.mutex = mutex

	def run(self):
		#Optmization check. Can suffer from race conditions, but it is going to be checked again 
		# on mutual exclucion
		if self.executed == 1:
			return #False

		ok = self._check_transition()
		if(not ok):
			return #False

		# lock
		self.mutex.acquire()
		
		if(self.executed == 0):
			self.executed = 1
		else:
			mutex.release()
			return# False

		self.mutex.release()


		#gera threads de execucao
		#join nas threads de exec
		exec_threads = self.__set_exec_threads()
		for thread in exec_threads:
			thread.join()
		
		# return True

	def _check_transition(self):
		#check all the pre conditions for a match, if theres any unmatching condition returns False
		for i in range(len(self.tapes)):
			print (self.tapes[i].read())
			print("Aqui ", self.transition.pre_conditions[i])
			if self.transition.pre_conditions[i] != self.tapes[i].read():
				return False
		return True

	def __set_exec_threads(self):
		#sets a threads for each tape
		exec_threads = []
		for i in range(len(self.tapes)):
			exec_threads.append(Executor(self.tapes[i], self.transition.post_conditions[i], self.transition.movements[i]))
			exec_threads[i].start()

		return exec_threads