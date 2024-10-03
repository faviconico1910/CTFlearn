
def Eating(s):
    return str(int(s)*a)

def concac(s, eats):
    print(s, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < len(s) and eat2 < len(eats):
        if eateat%a == c//b:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += s[eat1]
            eat1 += 1
        eateat += 1
    return eAt

def reverse(s):
    return s[::-1]

def eaT(s):
    return Eating(s[:a]) + reverse(s)



def Ate(s):
    return "Eat" + str(len(s)) + s[:a]


alpha = '0123456789'
s = ''
for i in alpha:
    for j in alpha:
        for k in alpha:
            s = i + j + k + 'eat009'
            a = 3
            b = a + 1
            c = a - 1
            eateat = concac(eaT(s), Ate(reverse(s)))
            if eateat == "E10a23t9090t9ae0140":
                flag = "eaten_" + s
                print("absolutely EATEN!!! CTFlearn{",flag,"}")
                exit(1)
            else:
                print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)



