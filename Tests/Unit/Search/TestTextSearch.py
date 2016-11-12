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
		text = textType('Tests/Sources/Texts/test2.txt')
		tiw = textIndexWriter(text)
		tir2 = textIndexReader('Indexes/test2.txt.text.index')
		triw = textReverseIndexWriter('Test.reverse.index', [tir, tir2])

	def ReverseIndexDeletion(self):
		os.remove('ReverseIndexes/Test.reverse.index.info')
		os.remove('ReverseIndexes/Test.reverse.index')
		pass

	def test_simpleSearch(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Test.reverse.index')
		search = textSearch('potatos', trir).computeResult()
		assert(search.query == 'potatos')
		assert(search.res[0] == 0)
		self.ReverseIndexDeletion()

	def test_complexSearch(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Test.reverse.index')
		search = textSearch('potatos freedom',trir).computeResult()
		assert(search.query == 'potatos freedom')
		assert(search.res[0] == 1)
		self.ReverseIndexDeletion()

	def test_noResult(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Test.reverse.index')
		search = textSearch('alice', trir).computeResult()
		assert(search.query == 'alice')
		assert(search.res == [])
		search.display()
		self.ReverseIndexDeletion()

if __name__ == '__main__':
    unittest.main()
