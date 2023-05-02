# rot13
def rot13(s):
    for i in s:
        if ord(i)<91 and ord(i)>=65:
            print(chr((((ord(i)-65)+13)%26)+65),end="")
        elif ord(i)>=97 and ord(i)<=122:
            print(chr((((ord(i)-97)+13)%26)+97),end="")
        else:
            print(i,end="") 
rot13("areibhf_jro_jzn")

# nervous_web_wma

