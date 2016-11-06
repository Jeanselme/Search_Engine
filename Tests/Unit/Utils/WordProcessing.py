"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys, os
# Needs to be execute from the project source
sys.path.append(os.getcwd())

import unittest
from Utils.WordProcessing import *

class TestWordProcessing(unittest.TestCase):

	def test_extractWords(self):
		simple = "Once upon a time"
		complex = "Once upon a time, in a far!"
		ponctu = "Once upon a time , in a far !"
		assert(len(extractWords(simple)) == 4)
		assert(len(extractWords(complex)) == 7)
		assert(len(extractWords(ponctu)) == 7)

	def test_stemming(self):
		simple = "Once upon a time"
		complex = "Once upon a time, in a far!"
		ponctu = "Once upon a time , in a far !"
		assert(len(stemming(extractWords(simple))) == 3)
		assert(len(stemming(extractWords(complex))) == 5)
		assert(len(stemming(extractWords(ponctu))) == 5)

if __name__ == '__main__':
    unittest.main()
