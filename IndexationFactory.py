"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from DocType.TextType import textType
from IndexManip.TextIndexManip import textIndexManip
from ReverseIndexManip.TextReverseIndexManip import textReverseIndexManip

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
		tims = []

		# Associates the good type of dataStructure and indexes before computing
		# the corresponding reverseIndexes
		for fileName in fileNames:
			dot = fileName.rfind('.')
			if fileName[dot:] in {".txt", ".md"} :
				tim = textIndexManip()
				text = textType(fileName)
				tim.create(text)
				tim.save()
				tims.append(tim)
			else:
				print("Error : Unknown format of " + fileName)

		textReverseIndexManip("ReverseIndexes/text.reverse.index").create(tims)
