#include<stdio.h>
#include<stdlib.h>

int main(){

	double count = 0;
	int n = 0;
	double distance = 0;
	while (n<6){
		int m = 0;
		while (m<6){
			distance+=abs(n-m);
			count+=1;
			m+=1;
		}
		n+=1;
	}

    printf("Total distance is ");
	printf("%f",distance);
    double avg = distance/count;
	printf("\nAvg.= ");
	printf("%f",avg);
    /* 1.944444444444  */
}
