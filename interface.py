'''
File Name: interface.py
Dependencies: calc.py
Purpose: Contains code that operates the interface of the calculator app 
(i.e mostly printing, running certain commands)
'''
import calc 
calculator = calc.Calc()

while True:
    user_input = input("Would you like to calculate your net income? y/n")
    if user_input == 'n':
        print("ok, have a good day!")
        break
    print("Great! First we must calculate your sales revenue.")
    user_input= input("Please provide us with your quantity sold:")
    quant_sold = int(user_input)
    user_input = input("Please provide us with your selling price per unit:")
    avg_sales_price = int(user_input)
    sales_revenue = calculator.sales_revenue_calc(quant_sold,avg_sales_price)
    print(f"Your sales revenue is {sales_revenue}")
    print("Great! Now we are going to calculate your cost of goods sold.")
    user_input = input("Please provide us with your opening inventory value:")
    open_inven = int(user_input)
    user_input = input("Please provide us with your purchase value:")
    purchases = int(user_input)
    user_input = input("Please provide us with your closing inventory value:")
    closing_inven = int(user_input)
    cogs_calc = calculator.cogs_calc(open_inven, purchases, closing_inven)
    print(f'Your COGS is {cogs_calc}! Now we will calculate your total expenses.')
    user_input = input("Please provide us with your total operating expenses:")
    operating_exp = int(user_input)
    total_exp_calc = calculator.total_exp_calc(operating_exp)
    print(f'Your total expenses equate to {total_exp_calc}')
    print('Now it is time to calculate your net income!')
    net_income = calculator.net_income_calc()
    print(net_income)

    user_input = input("Would you like to continue calculating another net income? y/n")
    
    # elif user_input == "n":
    #     print("Would you like to exit the program? y/n")
    #     break