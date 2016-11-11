"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os

# Modules for text documents
import DocType.TextType as TextType
import IndexManip.TextIndexManip as TextIndexManip
import ReverseIndexManip.TextReverseIndexManip as TextReverseIndexManip

"""
	key: file extension
	value: indexation key that can handle the corresponding file extension
"""
matching_key = {
	'.txt': 'text',
	'.md': 'text'
}

keys = ['text', 'unknown']

factory = {
	'text': {
		'doctype': TextType.textType,
		'reader': TextIndexManip.textIndexReader,
		'writer': TextIndexManip.textIndexWriter,
		'reverse_writer': TextReverseIndexManip.textReverseIndexWriter,
		'reverse_file_path': 'text.reverse.index',
	}
}


def group_by_key(documents):
	"""
		Groups documents by their indexation key (see get_matching_key)
	:param documents: List of documents
	:return: Dict where keys are from IndexationFactory.keys
					values are array with all document that matched
	"""
	grouped = {key: [] for key in keys}

	for document in documents:
		grouped[get_matching_key(document)].append(document)

	return grouped


def get_matching_key(document_path):
	"""
		Associate a document to the key of an indexation class that can handle it
	:param 	document_path: a document path to test
	:return: 	If the document can be handled, the corresponding indexation key
				Otherwise 'unknown'
	"""
	s = os.path.splitext(document_path)
	ext = s[1]

	key = matching_key[ext] if ext in matching_key else 'unknown'

	return key


def create_index_reader(key, document):
	"""
		Indexes the document and open a reader on the index file
	:param key:	should be the result of get_matching_key(document)
	:param document: Document to index
	:return: the corresponding reader object already initialized
	"""

	fac = factory[key]
	text = fac['doctype'](document)
	tiw = fac['writer'](text)

	return fac['reader'](tiw.savePath)


def create_reverse_indexes(documents):
	"""
		Indexes all documents according to their type and add them to their corresponding reverse index.
		All texts documents will be indexes through text indexation and added to the text reverse index
		Same for all future kind of document
	:param documents: List of documents. Should all exist !
	"""
	grouped = group_by_key(documents)
	for unknown in grouped['unknown']:
		print("No associated objects. Cannot index file: {}".format(unknown))

	del grouped['unknown']

	for key, docs in grouped.items():
		readers = []
		for doc in docs:
			readers.append(create_index_reader(key, doc))
		fac = factory[key]

		fac['reverse_writer'](fac['reverse_file_path'], readers)