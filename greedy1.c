#include <stdio.h>

int main() {
	int n,i, cnt, result;
	result=-1;
	cnt=0;
	scanf("%d",&n);

	for(i=0;i<=n/5;i++){
		if(n==3){
			result=1;
			break;
		}
		cnt=n-i*5;
		if(cnt%3==0){
			result=cnt/3+i;
		}
	}

	printf("%d",result);
	return 0;
}
