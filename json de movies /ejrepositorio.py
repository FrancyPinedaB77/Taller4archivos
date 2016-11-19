from __future__ import print_function

# a hack so you can run it 'python demo/search.py'
import sys

user_api_key = ")F1QD2RiHCaRVYYb5yc3cw(("

import stackexchange
so = stackexchange.Site("movies.stackexchange", app_key=user_api_key, impose_throttling=True)


a=0
if __name__ == '__main__':
    term = "a"

    qs = so.search(intitle=term)

	
    for q in qs:
#        print('%8d %s' % ( q.id,q.title))
        print('%8d %s' % ( q.id,q.title))
	a=a+1
print (a)
