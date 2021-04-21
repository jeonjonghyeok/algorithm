#include <stdio.h>
#include <stdlib.h>

int main()
{
  int i;
  int count=0;
  char a;
  int b;
  scanf("%c%d",&a,&b);

  int dx[] = {0,0,-2,2};
  int dy[] = {-2,2,0,0};
  int x,y;
  int temp;

  for(i=0;i<4;i++)
  {
    x=a-96;
    y=b;
    x += dx[i];
    y += dy[i];

    temp=y;
    if(i<2)
      temp=x;

    if(x>0 && y>0 && x<=8 && y<=8)
    {
      if(temp-1 >= 1)
        count++;
      if(temp+1 <= 8)
        count++;
    }
  }
  printf("%d\n",count);

  return 0;
}
