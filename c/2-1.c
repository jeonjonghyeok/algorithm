#include <stdio.h>

int main()
{
  int i,x_len,y_len, x, y;
  char n;
  char ns[] = {'R','R','R','U','D','D'};

  x=1;
  y=1;
  x_len = 5;
  y_len = 5;
  for(i=0;i<6;i++)
  {
    n= ns[i];
    if((n=='L' && x==1) || (n=='R' && x==x_len) || (n=='U'&&y==1) || (n=='D'&&y==y_len))
      continue;
    switch(n)
    {
      case 'R':
        x++;
        break;
      case 'L':
        x--;
        break;
      case 'U':
        y--;
        break;
      case 'D':
        y++;
        break;
    }
  }
  printf("x= %d, y= %d\n",y,x);
  return 0;
}
