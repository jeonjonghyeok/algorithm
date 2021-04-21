#include <stdio.h>

int main()
{
  int n,m, data;
  scanf("%d %d",&n,&m);

  int i,j;
  int min;
  int result = 0;
  for(i=0;i<n;i++)
  {
    min = 99;
    for(j=0;j<m;j++)
    {
      scanf("%d",&data);
      if(min > data) 
        min = data;
    }
    printf("min = %d\n",min);
    if(result < min) 
      result = min;
  }
  printf("%d",result);

  return 0;
}
