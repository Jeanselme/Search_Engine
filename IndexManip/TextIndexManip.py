"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from IndexManip.AbstractIndexManip import abstractIndexManip
import Utils.WordProcessing as wp
import re
from collections import Counter

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
		self.index = Counter(words)
		return self.index


	def readContinue(self):
		"""
		Reads and returns the next enter in the index (key, value)
		"""
		try:
			line = re.match(r"(?P<word>\w+):(?P<occurence>\d+)", self.ptr.readline())
			self.currentValue = [line.group("word"), line.group("occurence")]
		except Exception:
			self.currentValue = None

		return self.currentValue


	def save(self):
		"""
		Saves the index
		Word:Occurences
		"""
		self.savePath = "Indexes/" + self.source + self.signature
		with open(self.savePath, 'w') as dest:
			for word, number in sorted(self.index.items()):
				indexFormat = "{}:{}\n".format(word, number)
				dest.write(indexFormat)
		# Clear memory
		self.index = None
