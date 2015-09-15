class Transition:

	def __init__(self, preState,preConditions, postState,postConditions, movements):
		self.preConditions = preConditions #['a','b','c']
		self.postConditions = postConditions
		self.movements = movements
		self.preState = preState
		self.postState = postState




