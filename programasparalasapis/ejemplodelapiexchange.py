#import stackexchange
#so = stackexchange.movies.stackexchange()

#for q in so.questions(pagesize=50):
#    print q.title

import sys
from stackauth import StackAuth
from stackexchange import Site, StackOverflow

from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
comments = SITE.fetch('comments')