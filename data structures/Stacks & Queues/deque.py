from collections import deque
stack=deque()
#print(dir(stack))
#['__add__', '__class__', '__class_getitem__', '__contains__', '__copy__', '__delattr__', 
#'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#'__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
#'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 
#'insert', 'maxlen', 'pop', 'popleft', 'remove','reverse', 'rotate']
stack.append('ajay')
stack.append('anitha')
stack.append('raju')
stack.append('vinay')
stack.append('chinni')
#print(list(stack))
stack.pop()
print(list(stack))



