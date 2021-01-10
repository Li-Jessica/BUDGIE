## Running the application

### Using your Terminal:

### Dependencies:
* Python3.x
* pandas (Python3.x library)

### Steps:
1a. (For Windows Users): Open `cmd.exe` or `powershell.exe` and navigate to the application's folder

1b. (For Linux or Mac Users): Open your terminal and navigate to the application's folder

2. Enter the command `python main.py`

3. Have fun!

### Using the executable:

### Steps:

1. Run `main.exe`

2. That's it! 

## Inspiration
Although advances in technology have helped to spur various movements in youth education across the globe, we find that financial literacy remains an under-discussed topic in formal and informal youth education. We know that many female youth, ourselves included, often understand little about the management of personal finances, which is crucial towards achieving financial independence as an adult. By providing a simple budgeting application for such teenagers, we teach them to take control and be mindful of their spending at an early age, thus paving their way towards understanding finance management developing good money-managing habits that will last them a lifetime. 

## What it does
BUDGIE allows users to set personal budget goals and keep track of their balance, expenses, income, and budget use on a monthly basis. Users can enter in amounts of money they receive as “income”, and record various expenses associated with custom expense names. After the user enters a new transaction – ie. An income or expense – they can track the resulting changes in their total monthly balance using a check balance option. Most importantly, users can set a custom budget that can be easily modified by them if needed. Through the check budget function in BUDGIE, users who have set a valid budget can be reminded of how much their total monthly budget is, as well as how much of the current budget has been used and the amount that remains. If users exceed their stated budget, the budget check will alert them about this, in addition to indicating how much (in dollars) that they’ve exceeded their budget by. Aside from personal finance management, users can also browse the app‘s “About” and “Financial Tips” sections, which include detailed information about the app’s various functionalities and other useful beginner finance tips, including a guide to banking for youth. 

Additionally, the program also allows the user to print a concise record of the income, budget, and expenses that they have entered as a single csv file, which is named using the date of the user’s computer. The user can easily import this file into other data analysis programs for further processing if they wish to do so. 

## How we built it
We created BUDGIE using python and pandas. 

## Challenges we ran into
We faced quite a few challenges during the planning and development of our program as we were quite new to Python. The time constraints of the hackathon, required all of us to rapidly learn and adapt to using new tools including pandas and tkinter. We also had to try to find ways to efficiently implement the tools we had at hand in order to attain the goal we had in mind. At the same time, these challenges also pushed us out of our comfort zones to actively seek out novel learning opportunities and explore unfamiliar tools. Particularly during the coding process, we ran into many challenges with reading, writing, and row formatting for csv files. Since this type of file manipulation played a significant role in the operations of our program, ensuring proper usage was crucial at all stages of our project’s development. However, this did prove to be a great opportunity for us to take on new challenges and improve our proficiency in Python. Additionally, our challenges in the arduous testing and debugging process helped to raise our awareness of exceptions that may develop in program development and how important it is to ensure that they are resolved appropriately. 

## Accomplishments that we're proud of
Being students from different schools and backgrounds, this event provided us with a great opportunity to collaborate on a joint project for a field that we were all passionate about. We also became more proficient in Python, particularly in reading CSV files, coding loops, and writing if-else statements. 

## What we learned
As the majority of our team had little to no coding experience in Python, we found the SheHacks V workshops to be highly educational - particularly the Intro to Python workshop. Considering that this is our first hackathon, we were also able to learn a lot of coding techniques and etiquette from the more proficient members as we prepared and constructed our program.

## What's next for BUDGIE
In the future, we hope to expand the analytic ability of our program and improve the user interface to be more aesthetically appealing and friendly to youth. We attempted to try to create a GUI with Tkinker, however, due to the time constraint we were unable to finish it this time! In the future, we would like to modify the program so it can run on various other platforms. We would also like to implement the ability for the program to compute and conduct comparisons among a wider range of data points – e.g. Individual data values, totals, and expenses between weeks, months, and even years. This would allow the user to better track their spending over both short-term and long-term periods of their choosing. Finally, we would also love to take a more global approach by expanding BUDGIE to offer support for a wider range of languages and currencies.  
