def total(a, *numbers, **phonebook):
	print('a', a)
	
	for singel_item in numbers:
		print('singel_item', singel_item)
	
	for first_part, second_part in phonebook.items():
		print(first_part, second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))