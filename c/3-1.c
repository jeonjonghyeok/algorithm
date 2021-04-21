//stack
#include <stdio.h>
#include <stdlib.h>

#define QUEUE_SIZE 10

void push(int data);
int pop();

struct Stack 
{
  int *item;
  int top;
  int size;
};

struct Stack s;

int main()
{

  s.item = (int *)malloc(sizeof(int)*QUEUE_SIZE);
  s.top=-1;
  s.size =0;

  push(5);  
  push(2);
  push(3);
  push(7);
  printf("%d\n",pop());
  push(1);
  push(4);
  printf("%d\n",pop());
  printf("\n");

  int i;
  int size = s.size;
  for(i=0;i<size;i++)
  {
    printf("%d\n", pop());
  }


  return 0;
}

void push(int data)
{
  if(s.top >= QUEUE_SIZE)
  {
    printf("overflow\n");
    return;
  }
  s.item[++s.top] = data;
  s.size++;
}

int pop()
{
  if(s.top<0)
  {
    printf("underflow\n");
    return -1;
  }
  int result;
  result = s.item[s.top--];
  s.size--;
  return result;
}
