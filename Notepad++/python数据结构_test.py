set1 = set()
set1.add(1)
set1.add(1)
set1.add(2)
print(set1)
set1.update('1234')
print(set1)
set1.remove('1')
print(set1)
set1.discard('123')
set1.discard('3')
print(set1)