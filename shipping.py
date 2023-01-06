weight = 0
unit_price = 0

# Ground Shipping
flat_charge = 20

def groundshipping(weight):
    if weight <= 2:
        unit_price = 1.5
    if weight <= 2:
        unit_price = 1.5
    elif weight > 2 and weight <= 6:
         unit_price = 3.00
    elif weight > 6 and weight <= 10:
         unit_price = 4.00
    elif weight > 10:
         unit_price = 4.75
    cost = weight * unit_price + flat_charge
    return round(cost, 2)

# Premium Ground Shipping
def premiumgroundshipping():
    premium_flat_charge = 125
    return round(premium_flat_charge, 2)

# Drone Shipping
def droneshipping(weight):
    if weight <= 2:
        unit_price = 4.5
    elif weight > 2 and weight <= 6:
        unit_price = 9.00
    elif weight > 6 and weight <= 10:
        unit_price = 12.00
    elif weight > 10:
        unit_price = 14.25
    cost = weight * unit_price
    return round(cost, 2)

# Weight input from the user
weight = float(input("Enter weight of the package:"))
print("Ground Shipping Cost Total: " + "$" + str(groundshipping(weight)))
print("Premium Shipping Cost Total: " + "$" + str(premiumgroundshipping()))
print("Drone Shipping Cost Total: " + "$" + str(droneshipping(weight)))

if (groundshipping(weight) < premiumgroundshipping() and groundshipping(weight) < droneshipping(weight)):
    lowest_cost = groundshipping(weight)
    cheapest_method = "Ground Shipping"
elif (premiumgroundshipping() < droneshipping(weight) and premiumgroundshipping() < groundshipping(weight)):
    lowest_cost = premiumgroundshipping()
    cheapest_method = "Premium Ground Shipping"
else:
    lowest_cost = droneshipping(weight)
    cheapest_method = "Drone Shipping"

print(cheapest_method + " is the cheapest at: " + "$" + str(lowest_cost))