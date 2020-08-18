/*# 6 by 6 two-dimensional grid (no diagonal connections)
# (0,0,0,0)..(0,0,0,6)
# (0,0,0,1)..(0,0,0,7)
# (0,0,0,6)..(0,0,0,12)*/
#include<stdio.h>
#include <stdlib.h>
int main(){

	double d=0;
    int i=0;
    double count=0;
	while(i!=6){
		int j=0;
		while(j!=6){
			int k=0;
			while(k!=6){
				int n=0;
				while(n!=6){
					d+=abs(k-n)+abs(i-j);
					count+=1;
					n+=1;
				}
				k+=1;
			}
			j+=1;
		}
		i+=1;
	}

printf("Total length is %lf",d);
double avg = d/count;
printf("\nAvg.= ");
printf("%lf",avg);
/*# 3.888889*/
}
