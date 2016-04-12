__author__ = 'nacho'

import bug


B=bug.bug()


B._push('S',5)
B._push('S',6)
B._push('S',7)


B._dump_list(B._registers['S'])

while not B._is_empty(B._registers['S']):
    a=B._pop('S')
    print a

B._push('S',15)
B._push('S',16)
B._push('S',17)


while not B._is_empty(B._registers['S']):
    a=B._pop('S')
    print a


print a

