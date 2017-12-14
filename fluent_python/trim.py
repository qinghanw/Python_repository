'''def trim(s):
	i = 0
	j = 1
	if '' == s:
		return ''	
	while s[i] == ' ' and i < len(s)-1:
		i += 1
	while s[-(j+1)] == ' ' and j < len(s)-2:
		j += 1
	if i == len(s):
		return ''
	else:
		print('i = %d,j = %d'%(i,j))
		if j == 1:
			new = s[i:]
		else:		
			new = s[i:-j]
		print(new)
		return new
'''
def trim(s):
	if s == '':
		return s
	elif s[0] == ' ':
		return trim(s[1:])
	elif s[-1] == ' ':
		return trim(s[0:-1])
	else:
		return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')