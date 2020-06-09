#include <stdio.h>

//symbolic constants
//for f to c conversion
#define LOWER 0
#define UPPER 300
#define STEP 20
//for word count
#define IN 1 /* inside a word */
#define OUT 0 /* outside a word */


//function to convert temperature units
int fahrToCelsius(){
    float f,c;
    f = LOWER;
    while (f<=UPPER) {
        c = (5.0/9.0) * (f-32);
        printf("%3.0f Fahrenheit in Degree Celsius: %.1f\n",f,c);
        f = f+STEP;
    }
return 0;
}

//function to read and display characters on screen
int readChar(){
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}

//function prototype
int power(int ,int);

//function to count words and characters in one line
int countWords()
{
    int c, nl, nw, nc, state;
    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            break;
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT) {
            state = IN;
            ++nw;
        }
    }
    printf("Total words= %d; Total characters= %d\n", nw, nc);
}

int replaceSpaces(){
    int c, pc;
    pc = EOF;

    while ((c = getchar()) != EOF) {
        if (c == ' '){
            if (pc != ' ' && pc != '\t')
                putchar(c);
        }
        else if (c == '\t') {

            if (pc != ' ' || pc != '\t'){
                ;
            }
            else {
                putchar(' ');
            }

        }

        else if (c != ' '){
            putchar(c);
        }
        pc = c;
    }

    return 0;
}

int main()
{
    /*
    fahrToCelsius();
    readChar();
    int base=2;
    int n=2;
    int a= power(2,2);
    printf("%d raised to the power %d = %d\n",base,n, a);

    countWords();*/
    replaceSpaces();
    return 0;
}

int power(int base, int n)
{
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i)
    p = p * base;
    return p;
}
