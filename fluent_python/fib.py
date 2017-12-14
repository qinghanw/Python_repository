'''def fib(max):
	if 0 == max:
		return 0
	elif 1 == max:
		return 1
	return fib(max-1)+fib(max-2)

print(fib(50))
print('done')'''

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(500)