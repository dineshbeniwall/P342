
#include <stdio.h>

int main() {
    int s=1,m=0,n=0,t=0;
    printf("Integer input:");
    scanf("%d", &n);
   if (n >= 0){
       int i;
        for(i=1;i<=n;++i){
            s =s*i;
        }
        printf("factorial:%d", s);
   }
   else{
       m=-1*n;
        int i;
        for(i=1;i<=m;++i){
            s =s*i;
        }
        t=-1*s;
        printf("factorial:%d", t);
    }
    return 0;
}
