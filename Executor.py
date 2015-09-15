from threading import Thread

class  Executor(Thread):
	def __init__(self, tape, post_condition, movement):
		self.tape = tape
		self.post_condition = post_condition
		self.movement = movement

	def run(self):
		self.tape.write(post_condition)
		if movement == 'D':
			self.tape.move_head_up()
		elif movement == 'E':
			self.tape.move_head_down()
		return