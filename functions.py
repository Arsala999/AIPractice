'''
def pizza(crust, *toppings): #single * keeps more than on evalue : tuple
    print("You have ordered a pizza with " , crust, "crust and the following:" )
    for each in toppings:
        print(each)
pizza("thick","Green olives", "Chicken", "black olives")    
'''
def pizza(crust, **toppings):
    print("You have ordered a pizza with", crust , "crust the following")
    for key,value in toppings.items():
        print(key, ":", value)
pizza("Thick", toppings1 = "green olives", toppings2 = "chicken", toppings3 = "Green olives")  
