Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

Note that the walkthrough video for this project is slightly out of date — the walkthrough was done using a version of this project that uses functions. Feel free to come back to the video after having been introduced to functions!

1. First things first, define a weight variable and set it equal to any number.

2. Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

Write a comment that says “Ground Shipping”.

Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.


3. A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

8.4\ lb \times \$4.00 + \$20.00 = \$53.608.4 lb×$4.00+$20.00=$53.60
Test that your ground shipping function gets the same value.

Ground Shipping Premium:
4. We’ll also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.

5. Print it out for the user just in case they forgot!


6. Write a comment for this section of the code, “Drone Shipping”.

Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package 
of that weight.

7. A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

1.5\ lb \times \$4.50 + \$0.00 = \$6.751.5 lb×$4.50+$0.00=$6.75
Test that your drone shipping function gets the same value.
