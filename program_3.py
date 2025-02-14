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
#Loop through the years and months, adding up the rainfall.
    for year in range(years):
        for month in range(1,13):
            inches = float(input(f"Enter inches of rainfall for month #{month}(year #{year + 1}): "))
            rainfall += inches
#Print results in table format.
    print("\nMonths\t\tTotalInches\t\tAverage\n------------------------------------")
#Calculate average.
    average = rainfall / (years * 12)
#Now print values.
    print(f"{years * month}\t{rainfall:^25.2f}\t{average:.2f}")

if __name__ == '__main__':
    main()