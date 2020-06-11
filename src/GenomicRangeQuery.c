#include <stdio.h>

#define if_A 1
#define if_C 2
#define if_G 3
#define if_T 4


struct Results {
  int * A;
  int M; // Length of the array
};

int getImpactFactor(char s){
    if (s == 'A')
        return 1;
    else if (s == 'C')
        return 2;
    else if (s == 'G')
        return 3;
    else if (s =='T')
        return 4;
    else
        return 5;
}

struct Results solution(char *S, int P[], int Q[], int M) {
    int lowImpactFactor;
    int impactFactor;
    int *lif_array=calloc(M, sizeof(int)); // list to hold least impact factors
    struct Results result;
    for(int i=0; i<= M; i++) //
    {
        int lower = P[i];
        int upper = Q[i];


        if (lower == upper) {
            impactFactor =getImpactFactor(S[lower]);
             lif_array[i]=impactFactor;
        }
        else {
            for(int j=lower; j<=upper; j++){
                impactFactor = getImpactFactor(S[j]);
                if (impactFactor<lowImpactFactor){
                    lowImpactFactor=impactFactor;
                }
            }
            lif_array[i]=lowImpactFactor;
            lowImpactFactor=4;
        }
    }
    result.A = lif_array;
    result.M = M;
    return result;
}
