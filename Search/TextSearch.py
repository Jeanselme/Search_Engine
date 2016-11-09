"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from Search.AbstractSearchType import abstractSearchType
from Search.AbstractResult import abstractResult
import Utils.WordProcessing as wp
from collections import Counter

class firstTextResult(abstractResult):
	"""
	Prints the first result
	"""

	def display(self):
		if len(res) != 0:
			print(self.query + " has the words in common with " + self.res[0])
		else:
			print("No match in the current index")

class textSearch(abstractSearchType):
	"""
	Searchs through a reverseindex in order to find the text which has the most
	word in common with query
	Query has to be text
	"""

	def computeResult(self):
		"""
		Returns the result of the comparsion
		"""
		words = wp.extractWords(self.query)
		words = wp.stemming(words)
		indexedQuery = Counter(words)

		researchedWords = sorted(indexedQuery.keys())
		possibleDocs = []
		# Searchs the word in the reverse index
		for researchedWord in researchedWords:
			word, docFiles, values  = self.reverseIndex.readEntry()
			while word != '' and researchedWord > word:
				word, docFiles, values  = self.reverseIndex.readEntry()
			# When found it, add documents to the list
			if word == researchedWord:
				possibleDocs += docFiles

		res = None
		if len(possibleDocs) != 0:
			res = max(set(possibleDocs),key=possibleDocs.count)

		return firstTextResult(self.query, res)
