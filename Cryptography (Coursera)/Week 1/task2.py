__author__ = 'kroot'

import random

P = 295075153L   # about 2^28

class WeakPrng(object):
    def __init__(self, p):   # generate seed with 56 bits of entropy
        self.p = p
        self.x = 89059908L
        self.y = 164204369L
#        self.x = random.randint(0, p)
#        self.y = random.randint(0, p)

    def next(self):
        # x_{i+1} = 2*x_{i}+5  (mod p)
        self.x = (2*self.x + 5) % self.p

        # y_{i+1} = 3*y_{i}+7 (mod p)
        self.y = (3*self.y + 7) % self.p

        # z_{i+1} = x_{i+1} xor y_{i+1}
        return (self.x ^ self.y)

prng = WeakPrng(P)

for i in range(1, 11):
    print "output #%d: %d" % (i, prng.next())

#output #1: 210205973
#output #2: 22795300
#output #3: 58776750
#output #4: 121262470
#output #5: 264731963
#output #6: 140842553
#output #7: 242590528
#output #8: 195244728
#output #9: 86752752

#i = 0L
#range_i = 2**29L
#x = 0L
#y = 0L
#new_x = 0L
#new_y = 0L
#
#while i < range_i:
#    i+=1
#    x = i;
#    y = x ^ 210205973L;
#    new_x = (2*x + 5) % P
#    new_y = (3*y + 7) % P
#
#    if ((new_x ^ new_y) == 22795300L):
#        print "found at i = ", i, " x = ", x, " y = ", y
#        break
#    if ((i % 1000000) == 0):
#        print "progress = ", i

#found at i =  89059908  x =  89059908  y =  164204369
