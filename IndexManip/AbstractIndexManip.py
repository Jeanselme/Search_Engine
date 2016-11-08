"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractIndexManip:
	"""
	Manipulates the index
	Goal is to never have all the indexes in memory, it is why pointers are used
	for reading
	Abstract class
	"""

	def __init__(self):
		"""
		Creates all the different variables which are used for reading and witting
		"""
		# Signature -> Distinctive signature in order to check the format
		self.signature = ".index"

		## Reading
		# Pointer on the file
		self.ptr = None
		# Current read value
		self.currentValue = None

		## Writing
		# Name of the file
		self.source = None
		# Result of the index computation (create)
		self.index = None
		# Save Path
		self.savePath = None

	def create(self, docTypeFile):
		"""
		Creates the index after extracting the data of the given file
		Warning docTypeFile has to be adaptated to the current information
		extraction
		Abstract
		"""
		pass

	def readStart(self, fileName):
		"""
		Opens the file and initializes pointer in order to read it
		And reads the first entrance
		"""
		if (self.signature == fileName[-len(self.signature):]):
			self.ptr = open(fileName, 'r')
			return self.readContinue()
		else:
			print("Index is not in the good format")

	def readContinue(self):
		"""
		Reads and returns the next enter in the index (key, value)
		Abstract
		"""
		pass

	def save(self):
		"""
		Saves the index
		Abstract
		"""
		pass
