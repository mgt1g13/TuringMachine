from threading import Thread

class  Executor(Thread):
	def __init__(self, tape, post_condition, movement):
		Thread.__init__(self)
		self.tape = tape
		self.post_condition = post_condition
		self.movement = movement

	def run(self):
		self.tape.write(self.post_condition)

		if self.movement == 'D':
			self.tape.move_head_up()
		elif self.movement == 'E':
			self.tape.move_head_down()
		return