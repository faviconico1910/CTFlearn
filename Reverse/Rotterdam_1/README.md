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







