"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys, os, unittest
# Needs to be execute from the project source
sys.path.append(os.getcwd())

from DocType.TextType import *
from IndexManip.TextIndexManip import *
from ReverseIndexManip.TextReverseIndexManip import *
from Search.TextSearch import *

class TestTextSearch(unittest.TestCase):

	def ReverseIndexCreation(self):
		text = textType('Tests/Sources/Texts/test1.txt')
		tiw = textIndexWriter(text)
		tir = textIndexReader('Indexes/test1.txt.text.index')
		triw = textReverseIndexWriter('Text.reverse.index', [tir])

	def ReverseIndexDeletion(self):
		os.remove('ReverseIndexes/Text.reverse.index.info')
		os.remove('ReverseIndexes/Text.reverse.index')

	def test_simpleSearch(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Text.reverse.index')
		search = textSearch('potatos', trir).computeResult()
		assert(search.query == 'potatos')
		assert(search.res == 0)
		self.ReverseIndexDeletion()

	def test_noResult(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Text.reverse.index')
		search = textSearch('alice', trir).computeResult()
		assert(search.query == 'alice')
		assert(search.res == None)
		self.ReverseIndexDeletion()

if __name__ == '__main__':
    unittest.main()
