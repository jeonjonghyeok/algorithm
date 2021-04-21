#include <stdio.h>

int main()
{
  int n,m,k;
  int i, j;
  scanf("%d %d %d",&n,&m,&k);
  int array[n];
  for(i=0;i<n;i++)
    scanf("%d",&array[i]);
  int array_len;
  array_len = sizeof(array)/sizeof(int);

  int temp;
  for(i=0;i<array_len-1;i++)
  {
    for(j=i+1;j<array_len;j++)
    {
      if(array[i] > array[j])
      {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  int max, max_second;
  int m_count, s_count;

  max = array[array_len-1];
  max_second = array[array_len-2];
  
  m_count = m/(k+1)*k;
  m_count += m %(k+1);
  s_count = m%k;

  int result;
  result = m_count * max + s_count * max_second;
  printf("result = %d\n",result);

  return 0;
}
