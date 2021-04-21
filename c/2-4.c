#include <stdio.h>
#include <string.h>

int main()
{
  int n,m;
  int i,j;
  int x,y,direction;
  int dx[] = {0,1,0,-1};
  int dy[] = {-1,0,1,0};

  scanf("%d %d",&n,&m);
  int map[n][m];
  scanf("%d %d %d",&x,&y,&direction);

  for(i=0;i<n;i++)
    for(j=0;j<m;j++)
      scanf("%d",&map[i][j]);
  int gmap[n][m];
  int count=0;
  int nx, ny, rnx, rny;
  int turn_cnt=0;

  memcpy(gmap,map,sizeof(int)*m*n);
  gmap[y][x]=1;

  while(1)
  {
    if(direction==0)
      direction+=3;
    else
      direction--;
    turn_cnt++;

    nx = x+dx[direction];
    ny = y+dy[direction];
    printf("direction=%d, turn_cnt=%d, (%d %d), count=%d\n",direction, turn_cnt, nx,ny, count);

    if(direction < 2)
    {
      rnx = x+dx[direction+2];
      rny = y+dy[direction+2];

    }
    else
    {
      rnx = x+dx[direction-2];
      rny = y+dy[direction-2];
    }

    if(turn_cnt==4)
    {
      if(map[rny][rnx]==0 && rnx >= 0 && rnx  <= n && rny >= 0 && rny <= n)
      {
        x= rnx;
        y= rny;
        count++;
        turn_cnt=0;
        continue;
      }
      else
      {
        break;
      }
    }

    if(gmap[ny][nx]!=1 && nx >= 0 && nx <=n && ny >=0 && ny<=n)
    {
      gmap[ny][nx]=1;
      turn_cnt=0;
      x=nx;
      y=ny;
      count++;
      printf("direction=%d, turn_cnt=%d, (%d %d), count=%d\n",direction, turn_cnt, nx,ny, count);
      printf("\n");
    }
  }
  printf("%d",count);

  return 0;
}

