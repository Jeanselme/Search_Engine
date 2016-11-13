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
		if len(self.res) != 0:
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
		Returns the text with the most common words
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

		possibleDocs = sorted(set(possibleDocs),key=possibleDocs.count, reverse=True)
		possibleDocs = [self.reverseIndex.correspondingFile(doc) for doc in possibleDocs]

		return firstTextResult(self.query, possibleDocs)
