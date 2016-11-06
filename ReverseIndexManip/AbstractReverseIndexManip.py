"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractReverseIndexManip:
	"""
	Manipulates the reverse index
	Abstract class
	"""

	def __init__(self, fileName):
		"""
		Creates, extracts content, indexes and saves result
		Abstract
		"""
		# Signature -> Distinctive signature in order to check the format
		self.signature = None
		# Index file name
		self.reverseIndex = open(fileName, 'rw')
		# Current read value
		self.indexes = []
		# Documents in order to allow correspondance
		self.documentsNames = []

	def create(self, indexesFileNameList):
		"""
		Creates the reverse index by parcouring and comparing the different
		indexes
		Warning : indexesFile should be compatible with the object
		"""
		pass

	def write(self, key, document, value):
		"""
		Writes in the document the key and associated document and value
		Abstract
		"""
		pass

	def read(self):
		"""
		Reads and returns the next enter in the index (key, value)
		Abstract
		"""
		pass

	def correspondingFile(self, number):
		"""
		Returns the corresponding name of the file number
		"""
		assert(number < len(self.documents))
		return self.documents[number]

	@classmethod
	def merge(cls, indexesList, indexDestinationDirectory):
		"""
		Merges two Reverse indexes
		Abstract
		"""
		pass
