# SheHacks 2021 Submission
# Authors: Jessica Li, Rose Kim, Huiying Qin
# Description: display about and financial info

def about():
    print("""\nBUDGIE is your new favourite budget planning buddy! 
Does finance seem confusing and scary? If so, you have just found the
best tool to help you out! In this app, you can learn how to 
start managing your own budget! Starting from 
making personal budget goals, keep track of your balance,
and learn how to be responsible with your own money! 

This app contains 2 features you can use:

- Manage your Budget!
In this section, you can input your financial flows 
and keep a record of them on a monthly basis. 

You can keep track of: 
1. Income: Income is the money that you get 
2. Expenses: Expenses are the money you spend buying things
3. Total balance: For each new transaction, your balance will be updated!  
4. Budget: Your personal spending limit. (You don't want to exceed this!)
This app will allow you to make a budget goal on a monthly basis, and help you learn to be more financially mindful!

- Cool Financial Facts!
In this section, you can read more financial facts that will
help you improve your financial literature! """)

# Function to call menu 3 (Financial tips page).
def financialInfo():
    while True:
        print("\n========Welcome to the financial tips page!========")
        print("What would you like to know?")
        print("[1] What is a bank account?")
        print("[2] Why use a bank account?")
        print("[3] How to make a bank account?")
        print("[4] What is interest?")
        print("[5] What is credit?")
        print("[6] Go back to main menu")
        print("=================================================")

        user_input = input("Please enter your option: ")
        # tips for what is a bank account
        if user_input == "1":
            print('\nWhat is a bank account?\n')
            print("A bank account is an account you can set up\n"
                  "at a bank that allows you to store your money and also\n"
                  "records your transactions.\n\n"
                  "There are many types of bank accounts. If you are under\n"
                  "the age of majority (usually 18) in your province, you\n"
                  "can look into special youth savings accounts. These\n"
                  "accounts usually also come with special deals, and can\n"
                  "automatically convert to adult account types once you\n"
                  "are old enough.\n")
        # tips for why use a bank account
        elif user_input == "2":
            print('\nWhy use a bank account?\n')
            print("You don't need to know a lot about finances or\n"
                  "be stellar at math to get started. Banks welcome savers\n"
                  "of all ages and backgrounds!\n\n"
                  "Want to be more mature and prepared than your friends?\n"
                  "Having trouble saving up money for an expensive thing\n"
                  "you want to buy? Try managing your bank account and\n"
                  "learn how you can save your money for the things you\n"
                  "want! Is your jar, piggy bank, or wallet filling up?\n"
                  "Pop your cash in a bank, where it will be safe and\n"
                  "ready for you to use!\n")
        # tips for how to make a bank account
        elif user_input == "3":
            print('\nHow to make a bank account?\n')
            print("Disclaimer: this is geared towards Canadian citizens!\n\n"
                  "The application process in other countries may differ,\n"
                  "so always double check before applying.\n\n"
                  "If you are under the age of majority and are interested in\n"
                  "making a bank account, start by talking to your parents or\n"
                  "legal guardian(s) about it.\n\n"
                  "Together, you will need to book an appointment at a branch of\n"
                  "the bank you want to make your account at.\n\n"
                  "You will be told what you need to bring to the appointment,\n"
                  "usually your social insurance number (SIN) and some form(s)\n"
                  "of personal identification, such as your passport, or birth\n"
                  "certificate. It is important that you go with your guardian(s)\n"
                  "because the bank will need information from them as well.\n"
                  "As a teenager, it is important that you choose an account\n"
                  "type that doesn't charge a monthly/annual fee, doesn't have\n"
                  "a minimum balance, will earn you interest, and has, a fair\n"
                  "amount of free transactions for you to use.\n")
        # tips about interest
        elif user_input == "4":
            print("\nWhat is interest?\n")
            print("Interest is the cost applied to using someone else’s\n"
                  "money. Borrowers pay interest and the lenders earn interest.\n"
                  "You can also gain interest by depositing funds into an interest-\n"
                  "bearing bank account such as a savings account or a certificate\n"
                  "of deposit (CD). Interest is charged based on the interest rate,\n"
                  "which is given as the percentage of the borrowed amount in a\n"
                  "given time.\n")
        # tips about credit
        elif user_input == "5":
            print('\nWhat is credit?\n')
            print("Credit is an agreement between the lender and the\n"
                  "borrower in which a certain amount of money will be lent and has\n"
                  "to be paid back before the agreed time. If it is not paid on time,\n"
                  "an interest fee will be charged at an interest rate for you the pay\n"
                  "additionally. Other consequences include damage to your credit rating,\n"
                  "increases the interest rate on future credit usage and makes it more\n"
                  "difficult to take out car loans and buy a home in the future.\n\n"
                  "For a credit card, the user of the card is borrowing money\n"
                  "from the bank and during each billing cycle (typically per\n"
                  "month), they receive a bill to pay back to the bank.\n\n"
                  "Fun fact – having overdue books from the library can hurt\n"
                  "your credit score if you have not paid the overdue fine.\n")
        # exit condition
        elif user_input == "6":
            print("Hope you enjoyed your learning!")
            break
        # catch inputs not from 1-6
        else:
            print("Invalid input: please try again!")
