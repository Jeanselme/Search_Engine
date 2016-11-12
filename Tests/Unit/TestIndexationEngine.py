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
import IndexationEngine as iE


class TestIndexationEngine(unittest.TestCase):

	def test_force_argument(self):
		parser = iE.create_parser()
		arg = parser.parse_args(['--force', './IndexationEngine.py'])
		self.assertEqual(arg.force_indexation, True)

		arg = parser.parse_args(['./IndexationEngine.py'])
		self.assertEqual(arg.force_indexation, False)

	def test_documents_argument(self):
		parser = iE.create_parser()
		docs = ['./IndexationEngine.py']
		arg = parser.parse_args(docs)
		self.assertEqual(arg.documents, docs)

		docs2 = list(docs)
		docs2.append('dummy')

		arg = parser.parse_args(docs2)
		self.assertEqual(arg.documents, docs)


if __name__ == '__main__':
	unittest.main()
