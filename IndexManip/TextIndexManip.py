"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from IndexManip.AbstractIndexManip import abstractIndexManip
import Utils.WordProcessing as wp

class textIndexManip(abstractIndexManip):
	"""
	Manipulates texts indexes .text.index
	"""

	def __init__(self):
		abstractIndexManip.__init__(self)
		self.signature = ".text.index"

	def create(self, docTypeFile):
		"""
		Computes the index of the given text and return it as a dictionary of words
		and frequency
		"""
		self.source = docTypeFile.fileName
		words = docTypeFile.readContent()
		words = wp.extractWords(words)
		words = wp.stemming(words)
		self.index = {}
		for word in words:
			try:
				self.index[word] += 1
			except Exception as e:
				self.index[word] = 1
		return self.index


	def readContinue(self):
		"""
		Reads and returns the next enter in the index (key, value)
		Abstract
		"""
		pass


	def save(self):
		"""
		Saves the index
		Word:Occurences
		"""
		with open("Indexes/" + self.source + self.signature, 'w') as dest:
			for word, number in sorted(self.index.items()):
				indexFormat = "{}:{}\n".format(word, number)
				dest.write(indexFormat)