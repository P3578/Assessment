#include <stdio.h>
int main()
{ 
    int n1=180,n2=100,n3=120,n4=50,choose,i,q,a=0,b=0,c=0,d=0,sum;
    int k=0,l=0,m=0,n=0;
    up :
    printf ("\n 1. Pizza  price = %d rs/pcs",n1);
    printf ("\n 2. Burger price = %d rs/pcs",n2);
    printf ("\n 3. Dosa   price = %d rs/pcs",n3);
    printf ("\n 4. Idli   price = %d rs/pcs",n4);
    printf ("\n Please Enter your choose..... : ");
    scanf ("%d",&choose);
    switch(choose)
    {
        case 1:
        printf ("\n You have selected pizza.");
        printf ("\n Enter the quantity : ");
        scanf ("%d",&q);
             a = n1*q;
             printf ("\n Amount : %d",a);
             k  = k + a;
        break;
        case 2:
        printf ("\n You have selected Burger.");
        printf ("\n Enter the quantity : ");
        scanf ("%d",&q);
             b = n2*q;
             printf ("\n Amount : %d",b); 
             l  = l + a;
        break;
        case 3:
        printf ("\n You have selected Dosa.");
        printf ("\n Enter the quantity : ");
        scanf ("%d",&q);
             c = n3*q;
             printf ("\n Amount : %d",c); 
             m  = m + a;
        break;
        case 4:
        printf ("\n You have selected Idli.");
        printf ("\n Enter the quantity : ");
        scanf ("%d",&q);
             d = n4*q;
             printf ("\n Amount : %d",d);
             n  = n + a;
        break;
    }
    printf ("\n Do you want place more orders ? y & n : ");
    scanf (" %c",&choose);
    switch(choose)
    {
        case 'y':
            goto up;
        break;
        case 'n':
            goto down;
    } 
    down:
        sum = k+l+m+n;
       printf ("\n Total amount is = %d",sum);
    return 0;
}