def selection_sort(alist):
	for i in range(0, len(alist)-1):
		minnum_index = i;
		for j in range(i+1, len(alist)):
			if alist[j] < alist[minnum_index]:
				minnum_index = j
		if i != minnum_index:
			alist[i], alist[minnum_index] = alist[minnum_index], alist[i];

alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)