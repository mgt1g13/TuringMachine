class Transition:

	def __init__(self, pre_state,pre_conditions, post_state,post_conditions, movements):
		self.pre_conditions = pre_conditions #['a','b','c']
		self.post_conditions = post_conditions
		self.movements = movements
		self.pre_state = pre_state
		self.post_state = post_state




