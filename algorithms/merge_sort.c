#include <stdio.h>
#include <stdlib.h>

void merge(int * arr, int begin, int middle, int end)
{
	int i, j, k;
	printf("------------------------------begin\n");
	printf("begin = %d, middle = %d, end = %d\n", begin, middle, end);
	int left_size = middle - begin;
	int right_size = end - middle;
	int *left = (int *)malloc((left_size+1)*sizeof(int));	
	for(i = 0; i < left_size; i++)
	{
		left[i] = arr[begin+i];
	}	
	left[i] = 0x7fffffff;
	printf("i = %d\n", i);
	int *right = (int *)malloc((right_size+1)*sizeof(int));
	for(j = 0; j < right_size; j++)
	{
		right[j] = arr[middle+j];
	}
	right[j] = 0x7fffffff;
	printf("j = %d\n", j);
	
	i = 0;
	j = 0;
	for(k = begin; k < end; k++)
	{
		printf("left[%d]=%d, right[%d]=%d\n", i, left[i], j, right[j]);
		if(left[i] <= right[j])
		{
			arr[k] = left[i];
			i++;		
		}
		else
		{
			arr[k] = right[j];
			j++;
		}
		printf("i = %d, j = %d, arr[%d] = %d\n", i, j, k, arr[k]);
	}
	free(left);
	free(right);
	printf("-------------------------------end\n");
}

void merge_sort(int *arr, int begin, int end)
{
	if(begin+1 < end)
	{
		printf("begin = %d, end = %d\n", begin, end);
		int middle = (end + begin)/2;
		merge_sort(arr, begin, middle);
		merge_sort(arr, middle, end);
		merge(arr, begin, middle, end);
	}
}

int main()
{
	int i;
	int array[] = {3,41,52,26,38,57,9,49};	
	merge_sort(array, 0, 8);
	//int array[] = {5,2,4,7,1,3,2};
	//merge(array, 0, 3, 7);
	for(i = 0; i < sizeof(array)/sizeof(int); i++)
	{
		printf("%d\n", array[i]);	
	}
	return 0;	
}
