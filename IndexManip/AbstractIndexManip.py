"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os

class abstractIndexReader:
	"""
	Reads the index
	Goal is to never have all the indexes in memory, it is why pointers are used
	Abstract class
	"""

	def __init__(self, fileName):
		"""
		Creates all the different variables which are used for reading
		Opens the file and initializes pointer in order to read it
		"""
		## Reading
		# Pointer on the file
		self.ptr = open(fileName, 'r')
		# Current read value
		self.currentValue = None
		# Name of the file
		# TODO : Conserve this kind of information in a nother .info file
		self.source = os.path.basename(fileName)

		# To have a non empty currentValue
		self.readEntry()

	def readEntry(self):
		"""
		Reads and returns the next entry in the index (key, value)
		Abstract
		"""
		pass


class abstractIndexWriter:
	"""
	Writes the index
	Goal is to never have all the indexes in memory, it is why the index is destroyed
	at the end
	Abstract class
	"""

	def __init__(self,docTypeFile):
		"""
		Creates all the different variables which are used for writting in the file
		"""
		# Origin file
		self.source = docTypeFile
		# Result of the index computation (create)
		self.index = None
		# Save Path
		self.savePath = None
		# Creates the index
		self.create()
		# Saves index
		self.save()

	def create(self):
		"""
		Creates the index after extracting the data of the given file
		Warning docTypeFile has to be adaptated to the current information
		extraction
		Abstract
		Private
		"""
		pass

	def save(self):
		"""
		Saves the index and destroys the current index !
		Abstract
		Private
		"""
		pass
