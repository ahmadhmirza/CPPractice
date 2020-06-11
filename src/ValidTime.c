#include <stdio.h>
#include <stdlib.h>

void print(int *num, int n)
{
    int i;
    for ( i = 0 ; i < n ; i++)
        printf("%d ", num[i]);
    printf("\n");
}


int concatenate(int x, int y) {
    int pow = 10;
    while(y >= pow)
        pow *= 10;
    return x * pow + y;
}

int isValidHour(int A,int B){
  int hour = concatenate(A,B);
  if (hour <=23) {
      return 0;
  }
  else {
      return 1;
  }
}

int isValidmin(int A,int B){
  int min = concatenate(A,B);
  if (min <= 59 && min>=0) {
      return 0;
  }
  else {
      return 1;
  }
}

int solution(int A, int B, int C, int D){
    int num[4]={A,B,C,D};
    int temp;
    int status,status_1;
    int validHoursCount=0;
    for (int i = 1; i <= 4; i++) {
        for (int j = 0; j < 3; j++) {
            temp = num[j];
            num[j] = num[j+1];
            num[j+1] = temp;
            status= isValidHour(num[0],num[1]);
            if(status == 0){
                status_1 = isValidmin(num[2],num[3]);
                if (status_1 ==0) {
                    ++validHoursCount;
                    //validHoursCount= validHoursCount+1;
                }
            }
        }
    }
    printf("%d",validHoursCount);
	return validHoursCount;
}

/*int main()
{
    solution(1,2,3,4);
    return 0;
}*/
