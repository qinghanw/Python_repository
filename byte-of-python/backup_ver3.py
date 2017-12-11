import os
import time

source = ['"D:\\My Documents\\Python\\algorithms"']

target_dir = 'E:\\Backup'

#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + \
	comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully	created	directory',	today)
	
zip_command = '7z a {0} {1}'.format(target, ' '.join(source))

print('Zip Command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')
	