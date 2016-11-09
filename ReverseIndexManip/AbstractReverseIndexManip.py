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

	def __init__(self, fileName, read = False):
		"""
		Creates, extracts content, indexes and saves result
		If read is True, it is for read uses otherwise it is for write
		Abstract
		"""
		# Signature -> Distinctive signature in order to check the format
		self.signature = None
		# ReverseIndex file name
		self.reverseIndex = open(fileName, 'r' if read else 'w')
		# Current read value
		self.indexes = []
		# Documents in order to allow correspondance
		self.documentsNames = []

	def compare(self, key1, key2):
		"""
		Compares two keys
		Returns true if key1 > key2
		Abstarct
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


	def create(self, indexesFileManip):
		"""
		Creates the reverse index by parcouring and comparing the different
		indexes
		Warning : indexesFile should be compatible with the object
		This function is totally generic and should not be rewritten
		"""
		# Initialize all the new index manipulator
		for indexManip in indexesFileManip:
			self.indexes.append(indexManip)
			self.documentsNames.append(indexManip.source)
			indexManip.readStart(indexManip.savePath)

		while not self.endOfIndexes():
			key, documents, values = self.selectKey()
			self.write(key, documents, values)
			for doc in documents:
				# Read a new line of the different documents
				# from which we take a word
				self.indexes[doc].readContinue()

	def write(self, key, documentList, valueList):
		"""
		Writes in the document the key and associated document and value
		Private
		Abstract
		"""
		pass

	def read(self):
		"""
		Reads and returns the next enter in the Reverseindex (key, value)
		Abstract
		"""
		pass

	def endOfIndexes(self):
		"""
		Returns if all indexes have been fully readed
		Private
		"""
		for index in self.indexes:
			if index.currentValue != None:
				return False
		return True

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
		"""
		pass
