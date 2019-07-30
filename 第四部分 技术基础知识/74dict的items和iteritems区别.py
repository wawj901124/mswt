testl = {'key1':2,'key2':3,'key3':4}

kv1 = testl.items()
# print(next(kv1))

kv2 = testl.iteritems()   #py3没有这个函数
print(next(kv2))
print(next(kv2))
print(next(kv2))