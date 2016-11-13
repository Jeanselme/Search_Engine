"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import IndexationFactory

# directory where all reverse indexes can be found
directory = 'ReverseIndexes/'


def search(document_types, query):
	"""
		Searches through all reverse indexes that match the documents_types
	:param document_types: kind of document we are looking at (must mast IndexationFactory.factory keys)
	:param query: Set of words we are looking for in the indexed documents
	:return: array of results
	"""
	factory = IndexationFactory.factory

	results = []
	for doc_type in document_types:
		fac = factory[doc_type]
		reverse_file = directory + fac['reverse_file_path']
		reader = fac['reverse_reader'](reverse_file)
		search_result = fac['search'](query, reader).computeResult()
		results.append(search_result)

	return results


def display(results):
	"""
	:param results: Values returned by search
	:return: None
	"""
	for result in results:
		result.display()
