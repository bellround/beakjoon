#include <stdio.h>
int pi(int a)
{
    if (a <= 2)
    {
        return 1;
    }
    return pi(a-1) + pi(a-2);
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n == 0)
    {
        printf("0");
    }
    else{
    printf("%d",pi(n));}
    return 0;
}