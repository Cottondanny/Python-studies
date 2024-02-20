import math 

fnum=float(input("Please enter the first number:"))
operate=input("Please enter an operator:")
snum=float(input("Please enter the second number:"))

if operate=="+": 
    result=fnum+snum
    print("{} {} {} is {}".format(fnum,operate,snum,result))
elif operate=="-": 
    result=fnum-snum
    print("{} {} {} is {}".format(fnum,operate,snum,result))
elif operate=="*": 
    result=fnum*snum
    print("{} {} {} is {}".format(fnum,operate,snum,result))
elif operate=="/": 
    result=fnum/snum
    print("{} {} {} is {}".format(fnum,operate,snum,result))
else:
    print("You must enter an operator for this to work.")


