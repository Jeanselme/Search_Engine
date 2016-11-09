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

class TestWordProcessing(unittest.TestCase):

	def test_indexWrite(self):
		text = textType('Tests/Sources/Texts/test1.txt')
		tiw = textIndexWriter(text)
		assert(tiw.index == None)
		assert(os.path.exists('Indexes/test1.txt.text.index'))
		os.remove('Indexes/test1.txt.text.index')

	def test_indexRead(self):
		text = textType('Tests/Sources/Texts/test1.txt')
		tiw = textIndexWriter(text)
		tir = textIndexReader('Indexes/test1.txt.text.index')
		print(tir.source)
		assert(tir.source == 'test1.txt.text.index')
		assert(tir.currentValue == ['plur','4'])
		assert(tir.readEntry() == ['potato','3'])
		assert(tir.readEntry() == None)
		os.remove('Indexes/test1.txt.text.index')

if __name__ == '__main__':
    unittest.main()
