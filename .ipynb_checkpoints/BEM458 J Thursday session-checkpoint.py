#######################################################################################################################################################
# 
# Name: Charles Li
# SID: 750027911
# Exam Date: 27/03/2025
# Module: BEMM1458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-CharlesLi-exeter
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

# Loop through the dictionary using a for loop
for key in range(len(key_comments)):
    # Get the word to search for
    word = key_comments[key]
    
    # Find the start position of the word in the sentence
    start = customer_feedback.find(word)
    
    # Calculate the end position (start + length of the word)
    end = start + len(word)
    
    # Append the (start, end) tuple to my_list
    my_list.append((start, end))

# Print the result to verify
print(my_list)

#output : [(38, 50), (12, 17), (114, 120), (88, 94), (142, 150), (99, 109), (18, 28), (129, 136), (51, 58), (82, 87)]
#########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
first_two_digits = 75

# Insert last two digits of ID number here:
last_two_digits = 11

# Write your code for Operating Profit Margin
def operating_profit_margin(profit, revenue):
    if revenue == 0:
        return 0
    margin = (profit / revenue) * 100
    return margin

# Write your code for Revenue per Customer
def revenue_per_customer(revenue, customers):
    if customers == 0: # Avoid division by zero
        return 0
    rev_per_cust = revenue / customers
    return rev_per_cust

# Write your code for Customer Churn Rate
def customer_churn_rate(customers_lost, total_customers):
    if total_customers == 0:  # Avoid division by zero
        return 0
    # Ensure customers_lost doesn't exceed total_customers
    customers_lost = min(customers_lost, total_customers)
    churn = (customers_lost / total_customers) * 100
    return churn

# Write your code for Average Order Value
def average_order_value(revenue, orders):
    if orders == 0:  # Avoid division by zero
        return 0
    avg_order_val = revenue / orders
    return avg_order_val

# Call your designed functions here
profit_margin = operating_profit_margin(first_two_digits, last_two_digits)
rev_per_customer = revenue_per_customer(last_two_digits, first_two_digits)
churn_rate = customer_churn_rate(last_two_digits, first_two_digits)
avg_order_value = average_order_value(last_two_digits, first_two_digits)

# Print the results to verify
print(f"Operating Profit Margin: {profit_margin:.2f}%")
print(f"Revenue per Customer: {rev_per_customer:.2f} thousand")
print(f"Customer Churn Rate: {churn_rate:.2f}%")
print(f"Average Order Value: {avg_order_value:.2f} thousand")

#output :
#Operating Profit Margin: 681.82%
#Revenue per Customer: 0.15 thousand
#Customer Churn Rate: 14.67%
#Average Order Value: 0.15 thousand

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Define the data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1,1) #Reshape it into 2D 
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Step 2: Create and fit the linear regression model
model = LinearRegression()
model.fit(prices, demands)

# Get the slope (m) and intercept (b) of the linear model
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (m): {slope:.2f}")
print(f"Intercept (b): {intercept:.2f}")

# Step 3: Maximize revenue

a = slope
b = intercept
optimal_price = -b / ( 2 * a )
print(f"Price to maximize revenue: £{optimal_price:.2f}")

# Step 4: Predict demand at price = £52
price_to_predict = np.array([[52]])
predicted_demand = model.predict(price_to_predict)[0]
print(f"Demand at price £52: {predicted_demand:.2f} units")

# Output : 
#Slope (m): -4.48
#Intercept (b): 391.23
#Price to maximize revenue: £43.65
#Demand at price £52: 158.17 units
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: ")) # errors for the - 
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend()
plt.grid(True)
plt.show()

# errors for max-value,integer, marker='O',markercolor='green', ';', lable='Random Numbers', Line Chart of 100 Random Numbers,plt.legend('---')



