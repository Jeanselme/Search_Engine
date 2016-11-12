"""
    Search Engine
    by Vincent Jeanselme
    and Matthieu Clin
    vincent.jeanselme@gmail.com

    Indexation part from the Engine. Here we are indexing all documents in order to make them available trough
    later search
"""

import argparse
import os
import IndexationFactory


class CheckValidPath(argparse.Action):
    """
        Checks if each document provided is a valid path for a file
        Inspired from https://docs.python.org/3/library/argparse.html#action
        the FooAction class especially (end of the section)
    """
    def __call__(self, parser, namespace, values, option_string=None):

        valid_documents = []
        for document_path in values:
            if os.path.exists(document_path):
                valid_documents.append(document_path)
            else:
                print("Unknown path: {}".format(document_path))

        # settings valid_documents in the namespace
        setattr(namespace, self.dest, valid_documents)


def create_parser():
    """

    :return: Parser for the indexation engine.
                Looks for documents and keeps only the valid ones (file exists)
                Looks for optional attribute '--force'
    """
    p = argparse.ArgumentParser(description='Index the given files. All files provided will be available '
                                'for research purpose after the process')
    p.add_argument('--force', dest='force_indexation',
                   action='store_const',
                   const=True,
                   default=False,
                   help='If set, delete the indexation before computing. All previous documents added would be '
                   'removed from the engine !')

    p.add_argument('documents', nargs='+', action=CheckValidPath, help="List of documents to index")

    return p


def delete_indexes():
    """
        Deletes all files in directories that have extension in exts
    """
    directories = ['ReverseIndexes', 'Indexes']
    exts = ['.index', '.info']

    for directory in directories:
        for file in os.scandir(directory):
            s = os.path.splitext(file.name)
            ext = s[1]
            if ext in exts:
                os.remove(file.path)

if __name__ == '__main__':
    args = create_parser().parse_args()

    if args.force_indexation:
        delete_indexes()

    IndexationFactory.create_reverse_indexes(args.documents)
