# Making a calculater for rent of room/ flat 
#input we need from user
#total rent
#Electricity per unit 
#Charge per unit
#persons living in a room
#output(
#Total amount you to pay is 
rent = int(input("Enter the total rent of a room:"))
electricity = int(input("Enter the total electricity bill:"))
Charge_per_unit=int(input("Enter the charge per unit:"))
persons_living_in_room=int(input("Enter the number of person who lives in the room/Flat:"))
charges=electricity*Charge_per_unit
total_bill=Charge_per_unit+rent
output=total_bill/persons_living_in_room
print("Total amount you to pay is:", output)