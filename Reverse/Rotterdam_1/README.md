### Writeup for this challenge. It's quite complicated! 
We should use both IDA and GDB. 
Based on the challenge's description, we know that the flag kernel is the combination of 5 parts, which is a_b_c_d_e. We also know there is a function named "GetTData". This function returns a constant in rax register. So we don't need to care what it exactly does.
Before continuing, to be easier, I commented out every value while i was solving.
# Part1:
![image](https://github.com/user-attachments/assets/a381e4f9-9fe5-4969-8a5d-3990fffdcb2e)


This is the block of code to find out the first part of flag. Specifically, it moves the the first 8 bytes of our flag and xor with 0x2a460d92f5a1f504 (value from ``` ((_QWORD)v15 + v14)) ```, using GDB). Then, compare with 0x4B227FF781D59A56.

``` 0x4B227FF781D59A56 ^ 0x2a460d92f5a1f504 = 0x6164726574746f52 (adrettoR) => a = 'Rotterda'. ```
After each part of the flag, there will be an underscore '_' followed by the next part.

# Part2:

![image](https://github.com/user-attachments/assets/c7a8fa23-0818-4221-9e51-aa45c992113d)

![image](https://github.com/user-attachments/assets/fdb5e5da-f6d9-4001-9797-f6fe99375dff)

The value from GetTData function is 0x4f7fb8ade2f2cef6. Then, & 0x0FFFFFFFF, turn into 0xe2f2cef6.
This time, it gets the next four bytes from our input, add with 0xe2f2cef6 and compare with 0x15764FF46.
``` 0x15764ff46 - 0xe2f2cef6 = 0x74723050(tr0P) => b = 'P0rt' ```  

# Part3:
![image](https://github.com/user-attachments/assets/72092b5b-35b3-4dc3-93c5-b437833b55a9)

From the image, ``` v22 = 0xdeb4fa4d998c32ff => v25 = 0x4d998c32ff. v24 = our next 8 bytes & 0xFFFFFFFFFF ```. Finally, it compare ``` v24 - v25 ``` with 0x17D4A53553.
So, to obtain the this part, we'll use this fomular: ``` (0x17D4A53553 + 0x4d998c32ff) & 0xFFFFFFFFFF = 0x656e316852(en1hR) => c = 'Rh1ne' ```

# Part4:
![image](https://github.com/user-attachments/assets/25df0c4d-482c-47f5-8c87-2a20b8e98030)
 
![image](https://github.com/user-attachments/assets/bbb581a7-aed5-4bf6-b91a-9ced6112d137)

We have to know one thing, 64-bit register can only store 64 bits or 8 bytes => when using ``` mul ``` instruction, 8 left-most bytes will be stored in rax, 8 bytes higher in rdx. That's why the result of multiplication, which the program wants to be, is ``` 0x6A87544938037F7D400A77B9BE (be careful about the size of a register). ``` Therefore, we have this fomular ``` 0xdeb4fa4d998c32ff * (d & 0xFFFFFFFFFF) = 0x6A87544938037F7D400A77B9BE => d = 0x7a74316c42 = 'Bl1tz'  ```

# Part5
The last one, also the most complicated one.
![image](https://github.com/user-attachments/assets/fa873817-65ab-4725-87ed-6530312e0846)

When we observe the code in IDA, it can damage mental health because it's so confusing and frustrating. That's why the author suggested that we should learn Assembly. 

![image](https://github.com/user-attachments/assets/c62385aa-41d9-4405-9c21-eaab577072fd)

First, this block seems to be used to check the length of this part, it must be 5 characters. Then, equivalently, but a little different, it uses ``` div ``` instruction. The quotient of the division is stored in rax, the remainder in rdx.

![image](https://github.com/user-attachments/assets/7543558a-6b7e-4bd7-a014-21386343bd9e)

Therefore, we have this fomular 
```
0x1f6ff5218c40de9c / (e & 0x0FFFFFFFFFF) = 0x4F5352 remain 0x55930DBBE	
=> 0x4F5352 * (e & 0x0FFFFFFFFFF) + 0x55930DBBE = 0x1f6ff5218c40de9c
=> e = 'W1tte'
```

----------------------------------------------------------------------------------------------------------------------------------
### Flag: Rotterda_P0rt_Rh1ne_Bl1tz_W1tte











