# -*- coding: utf-8 -*-

from bitcoin import *
import timeit
import random
import os
import time


def main():
    privkey = random.randrange(2**256)
    search_for = 'tara'
    address = ''
    count = 0
    start = timeit.default_timer()
    pubkey_point = ''
    #address = address.lower()
    print "Searching for %s" % search_for

    while not search_for in address:
        privkey += 1
        pubkey_point = fast_multiply(G, privkey)
        address = pubkey_to_address(pubkey_point)
	address1 = address
	address=address.lower()
        count += 1
        if not count % 1000:
            print "Searched %d in %d seconds" % (count, timeit.default_timer()-start)

    print "Found address %s" % address1
    print "Private key HEX %s" % encode_privkey(privkey,'hex')
    pid = os.getpid()
    cmd = "kill -9 %d"%pid
    os.system(cmd)


if __name__ == '__main__':
    main()