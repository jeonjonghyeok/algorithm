#include <stdio.h>

int main()
{
  int n,k, count;
  scanf("%d %d",&n,&k);
  count = 0;

  while(n > 1)
  {
    printf("n=%d, count = %d\n",n,count);
    if(n > k) 
      count += n%k;
    n = n / k;
    count++;
  }

  printf("%d\n",count);
}
