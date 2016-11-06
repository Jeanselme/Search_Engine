"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from DocType.AbstractDocType import abstractDocType

class textType(abstractDocType):
	"""
	Different type of documents : .txt, .md
	"""

	def readContent(self):
		"""
		Extracts all content of the doc
		"""
		with open(self.path + self.fileName, 'r') as text:
			self.content = text.read()

		return self.content
