"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractDocType:
	"""
	Different type of documents : image, text
	Abstract class
	"""

	def __init__(self, fileName):
		"""
		Creates the structure for the file
		"""
		# Name of the original file
		self.fileName = fileName
		# Content of the file
		self.content = ""
		# Result of the indexation
		self.indexRes = {}

	def readContent(self):
		"""
		Reads the content of the file
		Abstract
		"""
		pass



	def index(self):
		"""
		Computes the indexed file
		Needs to have already extract the contents
		Abstract
		"""
		pass

	def save(self, indexDirectory):
		"""
		Saves the index of the document at the given indexDirectory
		Abstract
		"""
		pass
