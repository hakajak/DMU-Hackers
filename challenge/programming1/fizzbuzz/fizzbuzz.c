//FizzBuzz.c

#include <stdio.h>

main()
{
	for (int n=0; n<=100; n++)
	{
		if ( !(n % 3) && !(n % 5) ) printf ("FizzBuzz");
		else if (!(n % 3)) printf ("Fizz");
		else if (!(n % 5)) printf ("Buzz");
		else printf ("%d", n);
		
		printf("\n");
	}
}
