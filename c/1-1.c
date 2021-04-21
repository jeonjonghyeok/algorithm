
#include <stdio.h>

int main() 
{
  int n,i, count;
  n=1020;

  int money[] = {500,100,50,10};
  for(i=0;i<4;i++)
  {
    count += n/money[i];
    n = n%money[i];
  }
  printf("money=%d",count);

  return 0;
}


