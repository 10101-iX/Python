# This program on we calculat 2021 cash crop value

bori = input("\n>> Enter Number of Total Bori : ") # Get Input value of total bori
ll = float(bori * 40 )  #calculat total Kg 
Tl= float(ll / 100)  #we calculating here total Quintal
price = input("\n>> Enter Price of 1/Quintal : ")  #Getting input : price 
total = float(Tl * price )  # we calculating here Total Price 

#Print 
print("\n>> Weight " + "  :  "+  str(ll) + " Kg")
print ("\n>> Weight in Quintal " + "  :  "+ str(Tl) + " Q")
print("\n>> Total Value of " + str(Tl) + " Q" + "  :  "+ str(total) + " INR")
