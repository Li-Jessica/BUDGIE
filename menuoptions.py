# SheHacks 2021 Submission
# Authors: Jessica Li, Rose Kim, Huiying Qin
# Description: the budget planner

from Entry import Entry
import csv
import pandas as pd
import datetime
import os.path
from os import path

def budgetPlanner():
    filename = str(datetime.datetime.now().month) + str(datetime.datetime.now().year) + '_log' + '.csv'
    entryList = read_file(filename) # read specific csv file to list

    while True:
        # main budget menu
        print("\n========BUDGIE PLANNER MENU========")
        print("[1] Add income")
        print("[2] Add expense")
        print("[3] Set budget")
        print("[4] Check balance")
        print("[5] Check budget")
        print("[6] Display current records")
        print("[7] Go back to main menu")
        print("==================================")

        try:
            category = ""
            cost = 0
            budget = 0
            balance = 0 # total balance
            total_in = 0 # total income
            total_out = 0 # total expenses

            if not entryList: # if csv is empty, initiate the following values
                entryList.append([balance,total_in])  # 0 0, 0 1
                entryList.append([total_out, budget]) # 1 0, 1 1
            else:
                # entryList = [[balance, total_input], [total_out, budget] . . . ] <- looks like this
                balance = entryList[0][0]
                total_in = entryList[0][1]
                total_out = entryList[1][0]
                budget = entryList[1][1]

            option = int(input("Please select an option! "))

            if option == 1:
                category = "Income"
                print("Income", end="")
                cost = getMoneyInput()

                entryList[0][0] = float(entryList[0][0]) + cost # balance
                entryList[0][1] = float(entryList[0][1]) + cost # total_in

            elif option == 2:
                print("Expense ", end="")
                category = getInputName()

                print("Expense:", end="")
                cost = getMoneyInput()

                while cost > float(entryList[0][0]):
                    print("Expense cannot exceed current balance!")
                    print("Expense:", end="")
                    cost = getMoneyInput()

                entryList[0][0] = float(entryList[0][0]) - cost # balance
                entryList[1][0] = float(entryList[1][0]) + cost # total_out

            elif option == 3:
                print("Budget:", end="")
                budget = getMoneyInput()
                entryList[1][1] = budget

            elif option == 4:
                print("\nYour current balance is $%.2f" % float((entryList[0][0])))

            elif option == 5:
                if budget != 0:
                    print ("\nRemember, your monthly budget is $%.2f!" % (entryList[1][1]))
                    # portion of budget used (%)
                    budget_per = (float(entryList[1][0]) / float(entryList[1][1])) * 100
                    # print different things depending on if you've exceeded your budget or not
                    if budget_per >= 100:
                        # amount exceeded ($)
                        budget_exceed = float(entryList[1][0]) - float(entryList[1][1])
                        print ("\nYou've exceeded your current budget by $%.2f" % (budget_exceed) +" !\nYou have no budget left this month!")
                    else: # prints portion of budget spent
                        # remaining budget
                        budget_rem = float(entryList[1][1]) - float(entryList[1][0])
                        print("\nYour remaining budget for this month is $%.2f." % (budget_rem))
                        print("You've currently spent %.2f" % (budget_per) +"% of your monthly budget.")
                else:
                    print("\nYou currently have no budget set!")


            elif option == 6:
                print("\nTotal Income for %s, %s:" %(str(datetime.datetime.now().strftime("%b")),str(datetime.datetime.now().year)))
                if float(entryList[0][1]) == 0:
                    print("Your current total income is $0.00.\n")
                else:
                    income_count = 0
                    for income in entryList:
                        if income[0] == "Income":
                            income_count += 1
                            t_income = income[1]
                            print("Income entry {0:d}: {1:.2f}".format(income_count, t_income))
                    print("Your current total income is $%.2f\n" %float((entryList[0][1])))

                print("Total Expenses for %s, %s:" %(str(datetime.datetime.now().strftime("%b")),str(datetime.datetime.now().year)))

                if float(entryList[1][0]) == 0:
                    print("Your current total expenses is $0.00.")
                else:
                    # display expenses for this month (list them out)
                    for expense in entryList:
                        if expense[0] != 'Income' and expense[0] != 'nan' and expense[0] != "" and type(expense[0]) != float:
                            t_expense = expense[1]
                            print("Expense on {0:s}: {1:.2f}".format(expense[0], expense[1]))
                    print("Your current total expenses is $%.2f" %float((entryList[1][0])))

            elif option == 7:
                updateFile(entryList)
                return

            else:
                continue

            entry = Entry(category, cost)  # create entry object
            entryList.append([entry.category, entry.cost])

        except ValueError:
            print("Please try again!")

# get value
def getMoneyInput():
    while True:
        try:
            userIn = float(input(" $"))
            if userIn < 0:
                print("Value should be a positive number. ")
                continue
            else:
                return userIn
        except ValueError:
            print("Invalid entry!")

# get label input
def getInputName():
    userIn = input("[input label]: ")
    return userIn

# writes to csv file
def updateFile(lst):
    df = pd.DataFrame(lst)
    date = datetime.datetime.now()
    df.to_csv(str(date.month) + str(date.year) + '_log' + '.csv', index=False, header=False) # write for specific month

# reads and check if csv exists
def read_file(file_name):
    if (path.exists(file_name)):
        df = pd.read_csv(file_name, header=None)
        return df.values.tolist()
    else:
        return []
