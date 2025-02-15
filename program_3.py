#Program Written By: Ainsley Bellamy
#Date Written: 02/14/2025
#Program Title: Average_Rainfall


# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
#Get #years from user.
    years = int(input("Enter the number of years (whole number): "))
#Error handling.
    while years <= 0:
        years = int(input("~Error~ Please enter a valid number of years (whole number): "))
#Accumulator variable.
    rainfall = 0
#Dictionary with list values to hold number of inches for each month.
    months = {
        "January": [],
        "February": [],
        "March": [],
        "April": [],
        "May": [],
        "June": [],
        "July": [],
        "August": [],
        "September": [],
        "October": [],
        "November": [],
        "December": []
    }
#Another list to loop through.
    months_to_loop = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#Loop through the years and months, adding up the rainfall.
    for year in range(years):
        for month in months_to_loop:
            inches = float(input(f"Enter inches of rainfall for month #{month}(year #{year + 1}): "))
#Rainfall variable increases each time.
            rainfall += inches
#Add the inches value to its key in the dictionary.
            months[month].append(inches)
#Print results in table format.
    print("\nMonth\t\t\t\t\t\tAveragePerMonth\t\t\t\t\t\t\n-------------------------------------------")
#Loop to get each key from dictionary.
    for key, values in months.items():
        average = sum(values) / years
        print(f"{key:<20}\t\t{average:^20.2f}")
#Only print total rainfall once because it doesn't change.
    print(f"\nTotal Rainfall: {rainfall}")

if __name__ == '__main__':
    main()