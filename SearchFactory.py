"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class searchFactory:
	"""
	Class which associates the query to the corresponding type of data
	with the adaptated SearchType and ReverseIndexes
	"""

	def __init__(self, query):
		"""
		Inits the search with the query
		"""
		# Saves the query
		self.query = query

		# Associates the good type of data and reverseIndexes
