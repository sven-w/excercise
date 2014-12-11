#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
	{
		
		if (argc == 1)
			{
				printf("input the number and unit you want to convert, like: 12.3mil or 12.3mm\n");
				return 0;
			}
		
		double number;
		
		number = atof(argv[1]);
		
		if (strstr(argv[1], "mil"))
			{
				printf("%s = %.4fmm\n", argv[1], number*0.0254);
				return 0;
			}
			
		else if (strstr(argv[1], "inch"))
			{
				printf("%s = %.4fmm\n", argv[1], number*25.4);
				return 0;
			}
			
		else if (strstr(argv[1], "mm"))
			{
				printf("%s = %.4fmil\n", argv[1], number*39.37);
				return 0;
			}
			
		else
			{
				printf("unit support: mil, mm, inch\n");
				return 0;
			}
	}
		
		
