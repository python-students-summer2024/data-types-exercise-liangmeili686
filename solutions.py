"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """

    the_projected_amount_of_total_sales = input("What is the projected amount of total sales? ")
    profits = int(the_projected_amount_of_total_sales) * 23 / 100
    message = f'''"Profits: ${profits}" for sales of ${the_projected_amount_of_total_sales}''' 
    print(message)



def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    number_1 = input("Enter number #1: ")
    number_2 = input("Enter number #2: ")
    quotient = int(number_1) / int(number_2)
    remainder = int(number_1) % int(number_2)
    message = f"{number_2} goes into {number_1} a total of {quotient} times with a remainder of {remainder}"
    print(message)
          


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = input("Enter the miles driven: ")
    gas_used = input("Enter the gas used in gallons: ")
    miles_per_gallon = int(miles_driven) / int(gas_used) 
    print("Miles per gallon: " + str(miles_per_gallon))


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1 = input("Enter price #1: ")
    price2 = input("Enter price #2: ")
    price3 = input("Enter price #3: ")

    print("Here are your prices!")
    new_price_1 = format(float(price1),'.2f')
    new_price_2 = format(float(price2),'.2f')
    new_price_3 = format(float(price3),'.2f')

    message1 = format("Price #1: $" + format(str(new_price_1),'>10s'))
    message2 = format("Price #2: $" + format(str(new_price_2),'>10s'))
    message3 = format("Price #3: $" + format(str(new_price_3),'>10s'))
    print(message1)
    print(message2)
    print(message3)