#include <stdio.h>

int a[1001][1001];
int b[1001];
int v[1001];

int dfs(int s,int n)
{
    int q[10000] = {s};
    int ii = 0;
    int in = 1;
    while (ii != in)
    {
        int tem = q[ii++];
        if (v[tem] == 1)
        {
            continue;
        }
        v[tem] = 1;
        for (int i = 0; i < n; i++)
        {
            if (a[tem][i] == 1 && v[i] == 0)
            {
                q[in++] = i;
            }
        }
    }
    return 0;
}

int main()
{
    int n,m ;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n;i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    for (int i = 0; i < m;i++)
    {
        scanf("%d", &b[i]);
    }
    dfs(b[0] - 1, n);
    for (int i = 0; i < m; i++)
    {
        if (v[b[i] - 1] == 0)
        {
            printf("NO");
            return 0;
        }
    }
    printf("YES");
    return 0;
}