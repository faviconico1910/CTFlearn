# I wrote and debugged this code with all the convoluted "str(" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes


len = len
print = print
str = str




def EAt(input, eats):
    print(input, eats)
    i = 0
    j = 0
    k = 0
    result = ""
    while i < len(input) and j < len(eats):
        if k%a == c//b:
            result += eats[j]
            j += 1
        else:
            result += input[i]
            i += 1
        k += 1
    return result

def aten(input):
    return input[::a-b]

def Eating(input):
    return str((input)*a)
def eaT(input):
    return Eating(input[:a]) + aten(input)

def aTE(input):
    return input#*len(input)

def Ate(input):
    return "Eat" + str(len(input)) + input[:a]

def Eat(input):
    if len(input) == 9:
        if str.isdigit(input[:a]) and\
            str.isdigit(input[len(input)-a+1:]):
                eateat = EAt(eaT(input), Ate(aten(input)))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + input
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")
                else:
                    print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
        else:
            print("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad length :(")

print("what's the answer")
input = input()
a = len(input)//3
b = a+1
c = a-1
Eat(input)
