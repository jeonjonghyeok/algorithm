#include <stdio.h>

int main()
{
  int i,j,k;
  int count=0;
  int n;
  scanf("%d",&n);
  for(i=0;i<n+1;i++)
  {
    for(j=0;j<60;j++)
    {
      for(k=0;k<60;k++)
      {
        if(k%10==3 || j%10==3 || i%10==3 || k/10==3 || j/10==3)
          count++;
      }
    }
  }
  printf("%d\n",count);
  return 0;
}
