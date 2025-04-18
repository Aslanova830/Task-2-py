#1
def greeting(name):
    print(f"Salam,{name} ! Xoş gəldin.!")
name=input("Adin nedi?????????")
greeting(name)
###########################################
#2
def sum_numbers(a,b):
    print(a+b)
a=int(input('qiymet daxil edin'))  
b=int(input('qiymet daxil edin'))  
sum_numbers(a,b)
###########################################
#3
def  calculate_average(s):
    n=int(input("ne qeder eded olacaq"))
    for i in range(n): 
       num= int(input("eded daxil et"))
       s=s+num
    return s/n

numbers = calculate_average(0)
print(numbers)
