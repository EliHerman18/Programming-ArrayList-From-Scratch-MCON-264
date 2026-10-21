# main.py
from array_list import ArrayList

lst = ArrayList()

# add and size
lst.add("a")
lst.add("b")
lst.add("c")
print("size after 3 adds:", lst.size())          # 3

# getIndex
print("getIndex('b'):", lst.getIndex("b"))        # 1
print("getIndex('x'):", lst.getIndex("x"))        # -1

# remove
print("remove(1):", lst.remove(1))                # b
print("size after remove:", lst.size())           # 2
print("get(1):", lst.get(1))                      # c
print("getIndex('b'):", lst.getIndex("b"))        # -1

# set
lst.set(0, "z")
print("get(0) after set:", lst.get(0))            # z

# error case 1: bad index raises IndexError
try:
    lst.get(2)
except IndexError:
    print("get(2) raised IndexError")

# error case 2: full array raises OverflowError
full = ArrayList()
for i in range(100):
    full.add(i)
try:
    full.add(100)
except OverflowError:
    print("add to a full list raised OverflowError")