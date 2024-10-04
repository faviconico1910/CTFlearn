### Writeup for RE_verseDIS, pretty easy!

First, open the file in IDA, observe main function
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+8h] [rbp-8h]
  int j; // [rsp+Ch] [rbp-4h]

  printf("Input password: ");
  _isoc99_scanf("%s", input);
  for ( i = 0; i <= 21; ++i )
  {
    key2[i] = key[i];
    msg[i] = str[4 * i] ^ LOBYTE(key2[i]);
  }
  for ( j = 0; j <= 21; ++j )
  {
    if ( input[j] != msg[j] )
      stat = 0;
  }
  if ( stat )
    puts("Good job dude !!!");
  else
    puts("Wrong password");
  return 0;
}
```

We'll see it reads a string, then run a loop 21 times. In each iteration, it Xors key[i] with str[4 * i]. Click on key and str, we can see their value:


``` .data:0000000000201080 key             db 'IdontKnowWhatsGoingOn',0 ```
```
.data:0000000000201020 str             db 8, 3 dup(0), 6, 3 dup(0), 2Ch, 3 dup(0), 3Ah, 3 dup(0)
.data:0000000000201020                                         ; DATA XREF: main+8B↑o
.data:0000000000201030                 db 32h, 3 dup(0), 30h, 3 dup(0), 1Ch, 3 dup(0), 5Ch, 3 dup(0)
.data:0000000000201040                 db 1, 3 dup(0), 32h, 3 dup(0), 1Ah, 3 dup(0), 12h, 3 dup(0)
.data:0000000000201050                 db 45h, 3 dup(0), 1Dh, 3 dup(0), 20h, 3 dup(0), 30h, 3 dup(0)
.data:0000000000201060                 db 0Dh, 3 dup(0), 1Bh, 3 dup(0), 3, 3 dup(0), 7Ch, 3 dup(0)
.data:0000000000201070                 db 13h, 0Fh dup(0)
```
Finnaly, it compares the input with the the value has been XORed. We can easily write a script to derive the input, which is our flag. Here is my script:
```
key = 'IdontKnowWhatsGoingOn'
str = [ 0x08, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x2C, 0x00, 
0x00, 0x00, 0x3A, 0x00, 0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 
0x30, 0x00, 0x00, 0x00, 0x1C, 0x00, 0x00, 0x00, 0x5C, 0x00, 
0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 
0x1A, 0x00, 0x00, 0x00, 0x12, 0x00, 0x00, 0x00, 0x45, 0x00, 
0x00, 0x00, 0x1D, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 
0x30, 0x00, 0x00, 0x00, 0x0D, 0x00, 0x00, 0x00, 0x1B, 0x00, 
0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 
0x13, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

flag = ''
for i in range(0,21):
    flag += chr((str[4 * i] ^  ord(key[i])))

print(flag)
```

### Flag: AbCTF{r3vers1ng_dud3}
