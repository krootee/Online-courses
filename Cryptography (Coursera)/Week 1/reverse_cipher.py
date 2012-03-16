import array

m1 = array.array('B', "attack at dawn")
e1 = array.array('B', "6c73d5240a948c86981bc294814d".decode('hex'))
k1 = array.array('B')
m2 = array.array('B', "attack at dusk")
#e2 = array.array('B')
e2 = array.array('B', "6c73d5240a948c86981bc2808548".decode('hex'))
k2 = array.array('B')

#e2 = m2 ^ m1 ^ e1

for i in range(len(e1)):
#    e2.append(m2[i] ^ m1[i] ^ e1[i])
    k1.append(m1[i] ^ e1[i])
    k2.append(m2[i] ^ e2[i])

print m1
print m2
print "e1: ", e1
print "e1: ", e2
print k1
print k2
