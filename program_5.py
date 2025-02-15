# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():

#I renamed some of the variables. Budget
    budget = 0.0
#User gives the budget parameter.
    budget = float(input("Enter your planned budget for this month (as an integer): "))
#Controls how long the while loop runs; user controls that. Starts at 1 to get at least one iteration.
    control = 1
#User expense also, naturally, starts at 0.
    expense = 0
#Error handling for the budget amount.
    while budget < 0:
        budget = float(input("~Error~ Please enter a valid budget amount (as an integer): "))
#Runs to get each expense from user; they can exit if they change "control" to 0.
    while control != 0:
        control = float(input("Enter expense (one at a time) or press 0 to exit (as an integer): "))
#Error handling for the expense amount.
        while control < 0:
            control = float(input("~Error~ Please enter a valid expense amount (as an integer): "))
        expense += control
#Check if they went over budget.
    if expense > budget:
        debt = expense - budget
        print(f"\nYou seriously went over your budget and are now ${debt} in debt.")
#Else check if they were within or under budget.
    elif budget >= expense:
        reward = budget - expense
        print(f"\nGood job controlling yourself this month! You stayed within your budget"
              f" and saved ${reward}!")

if __name__ == '__main__':
    main()