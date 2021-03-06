#!/usr/bin/python

import sys
import parseterm

from functions_proof import *

term=sys.argv[1]
parsedterm=parseterm.parseterm(term)
if parsedterm is None:
    print "not a valid term!"
    sys.exit(0)
variables=parseterm.termvariables(parsedterm)
ind=parseterm.vindex(variables)
formulae=[]
freevariables=[]
l='lambda '+','.join(variables)+': '+term
v=ac.getterm2(l,variables,ind,formulae,freevariables)
if not formulae:
    print v
else:
    print "the result is",v
    formula=ac.composeformula(formulae,freevariables)
    print formula
