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

class TestTextReverseIndexManip(unittest.TestCase):

	def ReverseIndexCreation(self):
		text = textType('Tests/Sources/Texts/test1.txt')
		tiw = textIndexWriter(text)
		tir = textIndexReader('Indexes/test1.txt.text.index')
		triw = textReverseIndexWriter('Text.reverse.index', [tir])

	def ReverseIndexDeletion(self):
		os.remove('ReverseIndexes/Text.reverse.index.info')
		os.remove('ReverseIndexes/Text.reverse.index')

	def test_reverseIndexWrite(self):
		self.ReverseIndexCreation()
		assert(os.path.exists('ReverseIndexes/Text.reverse.index'))
		assert(os.path.exists('ReverseIndexes/Text.reverse.index.info'))
		self.ReverseIndexDeletion()

	def test_reverseIndexRead(self):
		self.ReverseIndexCreation()
		trir = textReverseIndexReader('ReverseIndexes/Text.reverse.index')
		assert(trir.readEntry() == ('plur', [0], [4]))
		assert(trir.readEntry() == ('potato', [0], [3]))
		assert(trir.readEntry() == (None, None, None))
		assert(trir.correspondingFile(0) == "test1.txt.text.index")
		self.ReverseIndexDeletion()

if __name__ == '__main__':
    unittest.main()
