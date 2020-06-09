#include <stdio.h>
/* copy input to output; 1st version */

int fahrToCelsius(){
    int f,c;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;

    f = lower;
    while (f<=upper) {
        c = 5 * (f-32) / 9;
        printf("%d Fahrenheit in Degree Celsius: %d\n",f,c);
        f = f+step;
    }
return 0;
}

int readChar(){
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}

int power(int ,int);

main()
{
    fahrToCelsius();
    //readChar();
    int base=2;
    int n=2;
    int a= power(2,2)
    printf("%d raised to the power %d = %d\n",base,n, a);
}

int power(int base, int n)
{
int i, p;
p = 1;
for (i = 1; i <= n; ++i)
p = p * base;
return p;
}
