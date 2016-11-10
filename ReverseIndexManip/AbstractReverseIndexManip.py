"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

class abstractReverseIndexReader:
	"""
	Reads the reverse index
	Abstract class
	"""

	def __init__(self, fileName):
		"""
		Initializes pointer to read reverseindex
		Abstract
		"""
		# ReverseIndex file name
		self.reverseIndex = open(fileName, 'r')
		# Documents in order to allow correspondance
		self.documentsNames = []
		with open(fileName + '.info') as info:
			self.documentsNames.append(info.readline().rstrip('\n'))

	def readEntry(self):
		"""
		Reads and returns the next entry in the Reverseindex (key, documentList, valueList)
		Abstract
		"""
		pass

	def correspondingFile(self, number):
		"""
		Returns the corresponding name of the file
		"""
		assert(number < len(self.documentsNames))
		return self.documentsNames[number]

	def __del__(self):
		"""
		Closes the pointer on the file
		"""
		self.reverseIndex.close()

class abstractReverseIndexWriter:
	"""
	Reads the reverse index
	Abstract class
	"""

	def __init__(self, fileName, indexesFileReader):
		"""
		Creates the reverse index by parcouring and comparing the different
		indexes
		Warning : indexesFile should be compatible with the object
		This function is totally generic and should not be rewritten
		"""
		# Oblige to have the result in the good folder
		fileName = 'ReverseIndexes/' + fileName
		# ReverseIndex file name
		self.reverseIndex = open(fileName, 'w')
		self.reverseIndexInfo = open(fileName + '.info', 'w')
		# Current read value
		self.indexes = []

		# Initialize all the new index manipulator
		for indexReader in indexesFileReader:
			self.indexes.append(indexReader)
			# Creates the different correspondance in the info file
			self.reverseIndexInfo.write(indexReader.source + '\n')
		while not self.endOfIndexes():
			key, documents, values = self.selectKey()
			self.write(key, documents, values)
			for doc in documents:
				# Read a new line of the different documents
				# from which we take a word
				self.indexes[doc].readEntry()

		# Close files
		self.reverseIndex.close()
		self.reverseIndexInfo.close()

	def compare(self, key1, key2):
		"""
		Compares two keys
		Returns true if key1 > key2
		Private
		"""
		return key1 > key2

	def selectKey(self):
		"""
		Selects the first key to put and returns docs and values
		Needs to have a non None key in the currentValue of the different indexes
		Private
		"""
		resKey = ''
		resDocuments = []
		resValues = []
		for index, i in zip(self.indexes, range(len(self.indexes))):
			if index.currentValue != None:
				key, value = index.currentValue[0], index.currentValue[1]
				if resKey == '' or self.compare(resKey,key):
					resKey = key
					resDocuments = [i]
					resValues = [value]
				# Same key => Adds the documentId
				elif resKey == key:
					resDocuments.append(i)
					resValues.append(value)

		return resKey, resDocuments, resValues

	def endOfIndexes(self):
		"""
		Returns if all indexes have been fully readed
		Private
		"""
		for index in self.indexes:
			if index.currentValue != None:
				return False
		return True

	def write(self, key, documentList, valueList):
		"""
		Writes in the document the key and associated documents and values
		Private
		Abstract
		"""
		pass
