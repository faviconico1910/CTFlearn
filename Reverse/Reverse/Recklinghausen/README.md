# Here is how I solved this challenge !!!

## Overview
In this challenge, the program first checks if an argument is provided. If no argument is supplied, it returns an error.

![image](https://github.com/user-attachments/assets/686b196d-3528-4c56-bbb2-081afb08521d)

After that, I use IDA to analyze it

![image](https://github.com/user-attachments/assets/26fb9390-bf32-4f1e-87dc-6acc9ba9df9a)

![image](https://github.com/user-attachments/assets/197ab89d-a3b6-4da7-8414-6646120f278f)


I just dont know about this function but I think the program will bypass this condition and jump to 'else if' branch

![image](https://github.com/user-attachments/assets/7d332a5f-962b-492d-9d26-7f2ccd3ec308)

Let's inspect CheckMsg function

z![image](https://github.com/user-attachments/assets/6a15731e-9759-401d-8f3b-d18d84c2454f)

![image](https://github.com/user-attachments/assets/5863a5b6-6268-4e96-b282-058900385861)

The function performs an XOR operation between BYTE_50E1 (0x7E) and each character of the provided argument (a1). A critical detail to note is that before the XOR operation, the program checks if the length of the argument is exactly 33 characters. If it is not, the program will return 0, effectively terminating the process.

To further investigate, I wanted to observe BYTE_50E2, which is relevant to our XOR operation. I set a breakpoint at its memory address and continued execution to examine its contents.

![image](https://github.com/user-attachments/assets/72774d6c-5477-47a8-acd3-e673470b685e)

After hitting the breakpoint, I gathered the necessary data:

![image](https://github.com/user-attachments/assets/a96eac60-9df3-44e6-ba75-f49148760d6a)

Finally, with all the gathered information, I arranged the results and wrote a simple exploit.py script to retrieve the flag.

![image](https://github.com/user-attachments/assets/ce7bd0a5-d639-49e3-b1c6-d09686ac3e85)


---------------------------------------------------
### Flag: CTFlearn{.......................}









