# list
# init
list = []
# add
list.append(obj)
list.insert(index, obj)
# delete
list.pop(index)
del list[index]
# search
list[:]
list[-1]

# dict
# init 
dict = {}
# add
dict.update({key:value})
dict.update('key' = value)# no!
#delete
dict.pop(key)
del dict[key]
# search
dict.items()
dict.keys()
dict[key]
# 
for key in dict.keys():
    print(key, dict[key], end = ' ')
print()

# set
set = set()
# add
set.add(obj)              # 1
set.update(objs)          # many
# delete
set.remove(obj)           # 1 warning
set.dicard(obj)           # 1 no waining
set.pop()                 # random
# & | -


