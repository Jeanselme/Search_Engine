"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys, os, unittest
# Needs to be execute from the project source
sys.path.append(os.getcwd())

from Utils.WordProcessing import *

class TestWordProcessing(unittest.TestCase):

	def test_extractWords(self):
		simpleS = "Once upon a time"
		longS = "Once upon a time, in a far!"
		ponctuS = "Once upon a time , in a far !"
		assert(len(extractWords(simpleS)) == 4)
		assert(len(extractWords(longS)) == 7)
		assert(len(extractWords(ponctuS)) == 7)

	def test_stemming(self):
		simpleS = "Once upon a time"
		longS = "Once upon a time, in a far!"
		ponctuS = "Once upon a time , in a far !"
		assert(len(stemming(extractWords(simpleS))) == 3)
		assert(len(stemming(extractWords(longS))) == 5)
		assert(len(stemming(extractWords(ponctuS))) == 5)

if __name__ == '__main__':
    unittest.main()
