print "Shared"
def func():
    res = []
    for i in xrange(0, 10):
        res.append(i)
    return i

func()
for i in xrange(0, 10):
    print i

