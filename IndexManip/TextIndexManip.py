"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import re
from collections import Counter
from IndexManip.AbstractIndexManip import abstractIndexReader, abstractIndexWriter
import Utils.WordProcessing as wp

class textIndexReader(abstractIndexReader):
	"""
	Reads texts indexes .text.index
	"""

	def readEntry(self):
		"""
		Reads and returns the next entry in the index (key, value)
		"""
		try:
			line = re.match(r"(?P<word>\w+):(?P<occurence>\d+)", self.ptr.readline())
			self.currentValue = [line.group("word"), line.group("occurence")]
		except Exception:
			self.currentValue = None
			self.ptr.close()

		return self.currentValue


class textIndexWriter(abstractIndexWriter):
	"""
	Writes texts indexes .text.index
	"""
	def create(self):
		"""
		Computes the index of the given text and return it as a dictionary of words
		and frequency
		"""
		words = self.source.readContent()
		words = wp.extractWords(words)
		words = wp.stemming(words)
		self.index = Counter(words)
		return self.index

	def save(self):
		"""
		Saves the index
		Word:Occurences
		"""
		self.savePath = "Indexes/" + self.source.fileName + '.text.index'
		with open(self.savePath, 'w') as dest:
			for word, number in sorted(self.index.items()):
				indexFormat = "{}:{}\n".format(word, number)
				dest.write(indexFormat)
		# Clear memory
		self.index = None
