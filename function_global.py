x = 50

def func():
	global x;
	
	print('x is', x)
	x = 2
	print('Changed local x to', x)

func()
print('Value of x is', x)