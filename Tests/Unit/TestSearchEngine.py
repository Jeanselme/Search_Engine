"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys
import os
import unittest
# Needs to be execute from the project source
sys.path.append(os.getcwd())
import SearchEngine as iE


class TestSearchEngine(unittest.TestCase):

	def test_no_document_types(self):
		parser = iE.create_parser()
		arg = parser.parse_args(['dummy query'])
		self.assertEqual(arg.document_types, None)

	def test_one_document_type(self):
		parser = iE.create_parser()
		arg = parser.parse_args(['dummy query', '-text'])
		self.assertEqual(arg.document_types, ['text'])

	def test_query(self):
		parser = iE.create_parser()
		arg = parser.parse_args(['dummy query'])
		self.assertEqual(arg.query, 'dummy query')

if __name__ == '__main__':
	unittest.main()
