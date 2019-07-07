'''
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
def add(n1,n2): #Receiving info / data called parameters
    my_sum=n1+n2
    print(my_sum)   
def sub(n1,n2):
    my_sum=n1-n2
    print(my_sum)
def mul(n1,n2):
    my_sum=n1*n2
    print(my_sum)
def div(n1,n2):
    my_sum=n1/n2
    print(my_sum)


c=str(input("Enter operation:"))
if c == '+':
    add(a,b)        
elif c == '-':
    sub(a,b)
elif c== '*':
    mul(a,b)
else:
    div(a,b)        

def my_pet(owner,pet):
    print(owner, "is an owner of " , pet)
my_pet(pet = "cat", owner = "Sarah" )        

#takes nothing returns sth
def sum():
    a=2
    b=3
    return(a+b)
result= sum()
print(result)
    
#takes sth returns sth
a=int(input("enter num 1:"))
b=int(input("Enter num 2:"))
def sum(val1,val2):
    result = val1+val2
    return result
output_of_function = sum(a,b)
print(output_of_function)

'''
#Even odd
a=int(input('Enter any number:'))
def evenodd(a):
    if a % 2==0:
        return('Even')
    else:
        return('odd')
b=evenodd(a)
print(b)

