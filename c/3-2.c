#include <stdio.h>
#include <stdlib.h>

#define QUEUE_SIZE 10

void enQueue(int data);
int deQueue();
int isPull();
int isEmpty();

int q[QUEUE_SIZE];
int front = -1;
int rear = -1;

int main()
{
  enQueue(5);
  enQueue(2);
  enQueue(3);
  enQueue(7);

  printf("%d\n",deQueue());
  printf("%d\n",deQueue());

  enQueue(1);
  enQueue(4);
  printf("%d\n",deQueue());
  printf("%d\n",deQueue());
  printf("%d\n",deQueue());
  printf("%d\n",deQueue());


  return 0;
}

int isPull()
{
  if(rear-front == QUEUE_SIZE)
    return 1;
  return 0;
}

int isEmpty()
{
  if(front == rear)
    return 1;
  return 0;

}

void enQueue(int data)
{
  if(isPull())
  {
    printf("over flow\n");
    return;
  }
  q[++rear]= data;
}

int deQueue()
{
  if(isEmpty())
  {
    printf("under flow\n");
    return -1;
  }
  front = (front+1)%QUEUE_SIZE;
  return q[front];
}
