# print (next(lst))
# tuples
tup = ("hello","world")
x = list(tup)
# x.append("!")  # instead of append, we can use insert too, but we will need two parameters in that case.
x.insert(1,"!")
y = tuple(x)
print(type(x))
print(tup,x,y)
# x.remove("hello") # to remove something from tuple.
y = tuple(x)
print(type(x))
print(tup,x,y)
del x[0] # to delete something from 
y = tuple(x)
print(type(x))
print(tup,x,y)