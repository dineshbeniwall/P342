#include<stdio.h>
#include<stdlib.h>
int main(){
    //Matrix M
	FILE *X;
	X = fopen("mat_m.txt","r");
	float m[3][3];
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			fscanf(X,"%f*%c", &m[i][j]);
		}
	}
	//matrix N
    FILE *Y;
	Y = fopen("N.txt","r");
	float n[3][3];
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			fscanf(Y,"%f*%c", &n[i][j]);
		}
	}
	//Matrix A
	FILE *Z;
	Z = fopen("A.txt","r");
	float a[3][1];
	for(int i=0;i<3;i++){
		for(int j=0;j<1;j++){
			fscanf(Z,"%f*%c", &a[i][j]);

		}
	}


	//matrix C =A*B
	float product[3][3]={};
    float ma[3][1] ={};
    // multipalication
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			for(int k=0;k<3;k++){
				product[i][j]+=m[i][k]*n[k][j];
                if (j==0){
                    ma[i][0]+=m[i][k]*a[k][0];
                }
			}
		}
	}
	// printing
    printf("Matrix multipalication M x N :\n");
    /*# M x N = [[0, 5, 0], [-2, -1, 1], [1, 2, -1]]*/
	for(int i=0; i<3; i++) {
      for(int j=0;j<3;j++) {
         	printf("%f ", product[i][j]);
         	if(j==2){
            printf("\n");
    		}
    	}
	}
	printf("\n Matrix multipalication M x A :\n");
    /*# M x A = [[6], [-2], [3]]*/
	for(int i=0; i<3; i++) {
      for(int j=0;j<1;j++) {
         	printf("%f ", ma[i][j]);
         	if(j==2){
            printf("\n");
    		}
    	}
	}

}
