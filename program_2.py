# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
#Request number of movies to determine how many times to run the loop.
    num_movies = int(input("How many movies would you like to enter? "))
#Error handling.
    while num_movies <= 0:
        num_movies = int(input("~Error~ Please enter a valid number of movies: "))
#Emptry dictionary to add to and draw from later.
    movies_tickets = {}
#Accumulator variable
    ticketNumTotal = 0
#Loop and ask for user input; starts at 1 so that the input requests do not display 0 at the start.
    for movie in range(1,num_movies + 1):
        movies = str(input(f"Enter movie number {movie} title: "))
        tickets = int(input(f"Enter number of tickets for movie number {movie}: "))
#Add iteration results to dictionary movies_tickets.
        movies_tickets[movies] = tickets
#Keep track of total number of tickets for all movies.
        ticketNumTotal += tickets
#Display results.
    print('Movies + Tickets:',movies_tickets,'\nTotal Number of Tickets:',ticketNumTotal)

if __name__ == '__main__':
    main()