hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create a variable, total_price, and set it to 0
total_price = 0

# Loop through the prices list and add each price to the variable total_price
for price in prices:
  total_price += price
print(total_price)

# Create a variable called average_price that is the total_price divided by the number of prices
average_price = total_price / len(prices)

# Print out the average_price
print("Average Haircut Price: " + str(average_price))

# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5
new_prices = [price - 5 for price in prices]

# Print new_prices
print(new_prices)

# Create a variable called total_revenue and set it to 0
total_revenue = 0

# Use a for loop to create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
# Add the product of prices[i] and last_week[i] to total_revenue at each step
  total_revenue += prices[i] * last_week[i]

# Print the value of total_revenue
print("Total Revenue: " + str(total_revenue))

# Find the daily revenue and assign it to a variable called average_daily_revenue
average_daily_revenue = total_revenue / 7

#Print out average_daily_revenue as an integer, not a floating point number
print(int(average_daily_revenue))

# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) -1) if prices[i] < 30]

# Print cuts_under_30
print(cuts_under_30)