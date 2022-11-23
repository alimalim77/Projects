#include<stdio.h>
#include<dos.h>
#include<conio.h>
void main()
{
 int h,m,s;

clrscr();
 textcolor(50+BLINK);
 cprintf("Please enter current time(//h:m:s):");
 scanf("%d %d %d",&h,&m,&s);
 again:
for(h;h<24;h++)
 {
  for(m;m<60;m++)
  {
   for(s;s<60;s++)
   {
    clrscr();
    textcolor(YELLOW)  ;
    gotoxy(20,20);
    cprintf("%d : %d : %d",h,m,s);
    delay(1000);
   }
   s=0;
  }
  m=0;
 }
 h=0;
 goto again;

 getch();
}
