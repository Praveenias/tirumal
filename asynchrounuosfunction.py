>>> def cube(x):
	return x*x*x
>>> cube(3)
27
>>> filter(lambda x:x%2,map(cube,range(1,11)))
<filter object at 0x00000204DCFFC8B0>
>>> s = filter(lambda x:x%2,map(cube,range(1,11)))
>>> s
<filter object at 0x00000204DCFFC220>
>>> s = list(filter(lambda x:x%2,map(cube,range(1,11))))
>>> s
[1, 27, 125, 343, 729]
>>> from functools import reduce
>>> s = reduce(lambda a,x:a+x,(filter(lambda x:x%2,map(cube,range(1,11)))))
>>> s
1225

