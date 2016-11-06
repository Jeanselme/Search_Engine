"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

"""
	Main programm
"""

import SearchFactory as sfac
import IndexationFactory as ifac

if __name__ == '__main__':
	ifac.indexationFactory(["Sources/Texts/AliceChapter1.txt", "Sources/Texts/AliceChapter2.md"])
