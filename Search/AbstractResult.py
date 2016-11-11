"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractResult:
	"""
	Results which are computed during a search execution
	Abstract class
	"""
	def __init__(self, query, res):
		"""
		Inits the result
		"""
		# Saves the res
		self.res = res
		# Saves the initial query
		self.query = query

	def display(self):
		"""
		Display the result
		Abstract
		"""
		pass
