# SheHacks 2021 Submission
# Authors: Jessica Li, Rose Kim, Huiying Qin
# Description: budgetPlanner main menu

from menuoptions import budgetPlanner
from otherMenuOptions import *

# main loop
while True:
    print("\n========WELCOME TO BUDGIE========")
    print("[1] Learn More About BUDGIE!")
    print("[2] Manage Your Budget!")
    print("[3] Financial Tips")
    print("[4] Exit")
    print("==================================")

    option = input("\nPlease enter your option! [Enter 1-4]: ")
    if option == "1":
        about()
        continue
    elif option == "2":
        budgetPlanner()
        continue
    elif option == "3":
        financialInfo()
    elif option == "4":
        print("\nProgram Terminating...")
        break;
    else:
        option = input("Please enter your option! [Enter 1-4]: ")
