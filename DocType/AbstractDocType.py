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
		slash = fileName.rfind('/')
		if slash != -1 :
			self.path = fileName[:slash+1]
			self.fileName = fileName[slash+1:]
		else:
			self.path = ""
			self.fileName = fileName
		# Content of the file
		self.content = None

	def readContent(self):
		"""
		Reads the content of the file
		Abstract
		"""
		pass
