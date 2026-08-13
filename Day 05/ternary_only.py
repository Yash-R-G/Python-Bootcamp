# title = "Movie Ticket Verification"

name = input("Enter your name : ")
age = int(input("Enter your age : "))
movie_rating = input("Enter the movie the movie rating to check the eligibility ( G, PG-13 ,R) : ")

status = "Eligible" if (movie_rating == "G" or (movie_rating == "PG-13" and age <= 13) or (movie_rating == "R" and age >= 18)) else "Not Eligible"

print("=" * 55)
print(f"{title:^55}")
print("=" * 55)

print(f"Customer Name : {name}\n")
print(f"Movie Rating : {movie_rating}\n")

print(f"Status : {status}\n")

print ("Enjoy your movie!\n" if status == "Eligible" else "Sorry, but you won't be able to watch\n")

print("=" * 55)
