"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class indexationFactory:
	"""
	Class which associates the fileNames with the associated docType and
	IndexManip before computing reverseIndexes
	"""

	def __init__(self, fileNames, force):
		"""
		Inits the indexation with the fileNames
		If force is true, the reindexation is computed
		"""
		# Saves the query
		self.fileNames = fileNames

		# Associates the good type of dataStructure and indexes before computing
		# the corresponding reverseIndexes
