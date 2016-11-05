"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractIndexManip:
	"""
	Manipulates the index
	Abstract class
	"""

	def __init__(self, fileName):
		"""
		Abstract
		"""
		# Signature -> Distinctive signature in order to check the format
		self.signature = ""
		# Index file name
		self.fileName = fileName
		# Pointer on the file
		self.ptr = open(index, "r")
		# Current read value
		self.currentValue = ""

	def create(self, docTypeFile):
		"""
		Creates the index after extracting the data of the given file
		Warning docTypeFile has to be adaptated to the current information
		extraction
		Abstract
		"""

	def readContinue(self):
		"""
		Reads and returns the next enter in the index (key, value)
		Abstract
		"""
		pass

	@classmethod
	def save(cls, index, indexDirectory):
		"""
		Saves the index at the given indexDirectory
		Abstract
		"""
		pass
