"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import re
from ReverseIndexManip.AbstractReverseIndexManip import abstractReverseIndexWriter, abstractReverseIndexReader

class textReverseIndexReader(abstractReverseIndexReader):
	"""
	Reads reverseindex for indexes .text.index
	"""

	def readEntry(self):
		"""
		Reads and returns the next entry in the Reverseindex (key, documentList, valueList)
		"""
		line = self.reverseIndex.readline()

		if line != '':
			line = re.match(r"(?P<word>\w+):(?P<docValue>\(\d+,\d+\)+)", line)
			word = line.group("word")
			docList = []
			valueList = []
			line = line.group("docValue")
			while line != '':
				line = re.match(r"\((?P<doc>\d+),(?P<value>\d+)\)(?P<docValue>(\(\d+,\d+\))*)", line)
				docList.append(int(line.group("doc")))
				valueList.append(int(line.group("value")))
				line = line.group("docValue")
			return word, docList, valueList
		else:
			return None, None, None


class textReverseIndexWriter(abstractReverseIndexWriter):
	"""
	Writes reverseindex for indexes .text.index
	"""

	def write(self, key, documentList, valueList):
		"""
		Writes in the document the key and associated documents and values
		word:(doc,occ)*
		"""
		self.reverseIndex.write(str(key) + ":")
		for doc, val in zip(documentList, valueList):
			revIndFor = "({},{})".format(doc, val)
			self.reverseIndex.write(revIndFor)
		self.reverseIndex.write('\n')
