#/usr/bin/python



s =  ''.join([line.rstrip() for line in open('sourcetext')])

OC = {}
for c in s: OC[c] = OC.get(c, 0) + 1


avgOC = len(s) // len(OC)
print ''.join([c for c in s if OC[c] < avgOC])
