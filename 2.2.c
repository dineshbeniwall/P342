#include<stdio.h>
/*# Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your
# choice in the code itself. Find A+B and A.B (dot product).*/
int main(){

	double A[3]={1, 2, 3};
	double B[3]={7, 8, 9};
	double sum[3] = {};
	double dot=0;

	for(int i=0;i<3;i++){
		dot+=A[i]*B[i];
        sum[i]=A[i]+B[i];
	}
	printf("A.B = %lf",dot);
    /*# 50*/
    printf("\nA+B = ");
    /*# [8, 10, 12]*/
    for(int i = 0 ; i < 3 ; i++)
    {
        printf("%lf\t",sum[i]);
    }
}
