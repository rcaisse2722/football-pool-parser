#!/usr/bin/env python

'''
usage:   extract.py <some.pdf>
Locates Form XObjects and Image XObjects within the PDF,
and creates a new PDF containing these -- one per page.
Resulting file will be named extract.<some.pdf>
'''

import sys

inpfn, = sys.argv[1:]

