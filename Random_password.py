import random
lower="abcdefghijklmnopqrstwxyz"
upper="ABCDEFGHIJKLMNOPQRSTWXYZ"
NUMBER="0123456789"
Symbol="@#$&_"
all=lower + upper + NUMBER +Symbol
length=8              
password="".join(random.sample(all,length))




print("The Password You Generated is : ",password)








