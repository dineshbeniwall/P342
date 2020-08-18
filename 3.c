#include <stdio.h>

int main() {
    double sum=1;
    double presum=0;
    double condition=1;
    double d,summ;
    int n,m;
    printf("Integer input:");
    scanf("%d", &n);
    if(n>0){
        for(int i=1;sum-presum>0.001 && condition==1;){
            if (i==n){condition=0;}
            else{
                i=i+1;
                d=i;
                presum=sum;
                sum=sum+1/d;
            }
        }
        printf("%lf\n", sum);
    }
    else if(n==0){printf("Sum is 1 or not defined as per the # QUESTION");}
    else{
        m=-n;
        for(int i=1;sum-presum>0.001 && condition==1;){
            if (i==m){condition=0;}
            else{
                i=i+1;
                d=i;
                presum=sum;
                sum=sum+1/d;
            }
        }
        summ=-sum;
        printf("%lf\n", summ);
    }
    return 0;
}
