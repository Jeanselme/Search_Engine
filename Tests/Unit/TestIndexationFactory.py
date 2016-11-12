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

import IndexationFactory


class TestIndexationEngine(unittest.TestCase):

    def test_txt_file(self):
        m = IndexationFactory.get_matching_key('myTextFile.txt')
        self.assertEqual(m, 'text')

    def test_md_file(self):
        m = IndexationFactory.get_matching_key('myTextFile.md')
        self.assertEqual(m, 'text')

    def test_unknown_extension_file(self):
        m = IndexationFactory.get_matching_key('myTextFile.unknown')
        self.assertEqual(m, 'unknown')

        m = IndexationFactory.get_matching_key('myTextFile.foobar')
        self.assertEqual(m, 'unknown')

    def test_no_extension_file(self):
        m = IndexationFactory.get_matching_key('myTextFile')
        self.assertEqual(m, 'unknown')

    def test_group_texts(self):
        docs = ['file1.txt', 'file2.txt']
        grouped = IndexationFactory.group_by_key(docs)
        expected = {'text': docs, 'unknown': []}
        self.assertDictEqual(grouped, expected)

    def test_group_texts_and_mds(self):
        docs = ['file1.txt', 'file2.md']
        grouped = IndexationFactory.group_by_key(docs)
        expected = {'text': docs, 'unknown': []}
        self.assertDictEqual(grouped, expected)

    def test_group_texts_and_unknowns(self):
        docs = ['file1.txt', 'file2.fake_extension']
        grouped = IndexationFactory.group_by_key(docs)
        expected = {'text': [docs[0]], 'unknown': [docs[1]]}
        self.assertDictEqual(grouped, expected)

    def test_create_index(self):
        reader = IndexationFactory.create_index_reader('text', './Tests/Sources/Texts/test1.txt')
        assert (os.path.exists('Indexes/test1.txt.text.index'))
        os.remove('Indexes/test1.txt.text.index')

if __name__ == '__main__':
    unittest.main()
