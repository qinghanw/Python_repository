#include <stdio.h>

int main(int argc, char ** argv)
{
	int array[] = {5, 2, 4, 6, 1, 3};	
	int i, j, tmep;
	for(i = 1; i < sizeof(array)/sizeof(int); i++)	
	{
		tmep = array[i];
		j = i - 1;	
		while(j >= 0 && array[j] < tmep)
		{
			array[j+1] = array[j];
			j = j - 1;
		}
		array[j+1] = tmep;
	}
	for(i = 0; i < sizeof(array)/sizeof(int); i++ )
	{
		printf("%d\n", array[i]);	
	}
	return 0;		
}
