"""
    Search Engine
    by Vincent Jeanselme
    and Matthieu Clin
    vincent.jeanselme@gmail.com
"""

import argparse
import SearchFactory

"""
    List of available document types search
    An entry corresponds to a kind of document the user can look for.
    Example : The first entry is '-text' meaning that the user can search through text documents
"""
document_args = [
    {
        "arg": "-text",
        "value": "text",
        "help": 'If set, includes all text documents in the research (.txt and .md)'
    }, {
        "arg": "-image",
        "value": "image",
        "help": 'If set, includes all images in the research (.jpg and .png)'
    }
]


def create_parser():
    """
        Includes all arguments available in the document_args array
        Adding or removing a document type should be done before calling this method
    :return: Parser for the SearchEngine
    """
    p = argparse.ArgumentParser(description='Search through indexed files. By default looks into all '
                                            'documents no matter their type')

    for arg in document_args:
        p.add_argument(arg['arg'],
                       dest='document_types',
                       action='append_const',
                       const=arg['value'],
                       help=arg['value'])

    p.add_argument('query',
                   help='Query for the search engine. Should be a string')

    return p


if __name__ == '__main__':
    # as image research is not available at the moment, removing it
    del document_args[1]

    args = create_parser().parse_args()

    # if no document_types are provided, we take them all into account
    if args.document_types is None:
        values = [doc['value'] for doc in document_args]
        args.document_types = values

    results = SearchFactory.search(args.document_types, args.query)
    SearchFactory.display(results)
