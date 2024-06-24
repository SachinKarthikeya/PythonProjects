import numpy as np
import pandas as pd
from datetime import date

#Creating empty lists for goods-services, prices, dates and expense types
goods_or_services = []
prices = []
dates = []
expense_types = []

#Adding the expenses to the lists to organize the data
def add_expense(good_or_service, price, date, expense_type):
    goods_or_services.append(good_or_service)
    prices.append(price)
    dates.append(date)
    expense_types.append(expense_type)

option = -1
while (option != 0):
    #Create an option menu
    print("Welcome the the Expense Tracker! The options are as follows:")
    print("0. Exit")
    print("1. Add Food Expense")
    print("2. Add Household Expense")
    print("3. Add Transportation Expense")
    print("4. Save and Show the expenses report")
    option = input("Choose an option: ")

    if option == '0':
        print("Thank You for choosing our system.")
        break
    elif option == '1':
        print("Adding Food...")
        expense_type = 'FOOD'
    elif option == '2':
        print("Adding Household...")
        expense_type = 'HOUSEHOLD'
    elif option == '3':
        print("Adding Transportation...")
        expense_type = 'TRANSPORTATION'
    elif option == '4':
        expense_report = pd.DataFrame() #Create a Data Frame for adding expenses                        
        expense_report['Goods_or_Services'] = goods_or_services
        expense_report['Prices'] = prices
        expense_report['Dates'] = dates
        expense_report['Expense_Types'] = expense_types
        expense_report.to_csv("expenses.csv") #Saving the report in the form of a CSV File
        print(expense_report) 
    else:
        print("Incorrect Choice!! Choose from the given Menu.") 

    #Allowing the user to enter the desired expenses
    if option == '1' or option == '2' or option == '3':
        good_or_service = input("Enter the good or service: ")
        price = float(input("Enter the price: "))
        today = date.today()
        add_expense(good_or_service, price, today, expense_type)
    print()