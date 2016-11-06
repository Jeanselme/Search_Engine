"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from DocType.TextType import textType
from IndexManip.TextIndexManip import textIndexManip

class indexationFactory:
	"""
	Class which associates the fileNames with the associated docType and
	IndexManip before computing reverseIndexes
	"""

	def __init__(self, fileNames, force = False):
		"""
		Inits the indexation with the fileNames
		If force is true, the reindexation is computed
		"""
		# Init all the different index
		tim = textIndexManip()

		# Associates the good type of dataStructure and indexes before computing
		# the corresponding reverseIndexes
		for fileName in fileNames:
			dot = fileName.rfind('.')
			if fileName[dot:] in {".txt", ".md"} :
				text = textType(fileName)
				tim.create(text)
				tim.save()
			else:
				print("Error : Unknown format of " + fileName)
