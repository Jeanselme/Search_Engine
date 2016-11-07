"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from ReverseIndexManip.AbstractReverseIndexManip import abstractReverseIndexManip
from IndexManip.TextIndexManip import textIndexManip

class textReverseIndexManip(abstractReverseIndexManip):
	"""
	Creates and manipulates reverseindex from indexes
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


	def read(self):
		"""
		Reads and returns the next enter in the index (key, value)
		Abstract
		"""
		pass
