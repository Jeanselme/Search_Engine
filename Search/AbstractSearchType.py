"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractSearchType:
	"""
	Searchs through a certain type of index with a specific computing method
	Abstract class
	"""
	def __init__(self, query, reverseIndex):
		"""
		Inits the search with the query
		"""
		# Saves the query
		self.query = query
		# Open associated reverseIndex
		self.reverseIndex = reverseIndex

	def computeResult(self):
		"""
		Returns the result of the comparsion
		Do not forget to close the reverseIndex
		Abstract
		"""
		pass
