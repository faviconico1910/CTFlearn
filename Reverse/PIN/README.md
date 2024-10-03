### This challenge is really, really easy!!
Let's just jump into IDA, decompile it, we'll see cek function 

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+Ch] [rbp-4h] BYREF

  printf("Masukan PIN = ");
  __isoc99_scanf("%d", &v4);
  if ( cek(v4) )
    puts("PIN benar ! \n");
  else
    puts("PIN salah ! \n");
  return 0;
}
```
Click on this function, we can see it clearly
```
_BOOL8 __fastcall cek(int a1)
{
  return a1 == valid;
}
``
Then, click on valid, we'll see it's value
``` .data:0000000000601040 valid           dd 51615h ```

Overall, this challenge reads an input and check if it equals to 0x51615 -> TRUE, else FALSE
But we notice that "%d" so we have to type the decimal of 0x51615, which is 333333

