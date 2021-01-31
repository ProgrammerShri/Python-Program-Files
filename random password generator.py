import random                                #import random library
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*:/,_-"

all = lower + upper + numbers + symbols
length = 16                                 #lenght of random password
password = "".join(random.sample(all,length))
print(password)                             #print random password