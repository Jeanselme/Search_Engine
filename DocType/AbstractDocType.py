"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os

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
		self.path = os.path.dirname(fileName)
		self.fileName = os.path.basename(fileName)
		# Content of the file
		self.content = None

	def readContent(self):
		"""
		Reads the content of the file
		Abstract
		"""
		pass
