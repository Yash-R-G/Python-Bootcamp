customer_name = input("Enter your name : ") 
movie_name = input(f"Hello {customer_name}, Enter the movie name : ")
number_of_tickets = int(input(f"How many tickets do you want for {movie_name} : "))
price_per_ticket = float(input("Enter the single ticket price : ₹"))
snack_cost = float(input("Enter the snack cost, if none then 0 : ₹"))
parking_fee = float(input("Enter the Parking fee, if not applicable then 0 : ₹"))

ticket_cost = number_of_tickets * price_per_ticket
subtotal = ticket_cost + snack_cost + parking_fee
gst = subtotal * 0.18
grand_total = subtotal + gst
cost_per_person = grand_total / number_of_tickets

title = "Movie Receipt"

print(f"\n{title:=^55}\n")

print(f"Customer Name   : {customer_name}")
print(f"Movie           : {movie_name}\n")
print(f"Tickets         : {number_of_tickets}")
print(f"Price/Ticket    : ₹{price_per_ticket:.2f}\n")
print(f"Ticket Cost     : ₹{ticket_cost:.2f}")
print(f"Snack Cost      : ₹{snack_cost:.2f}")
print(f"Parking Fee     : ₹{parking_fee:.2f}\n")
print(f"Subtotal        : ₹{subtotal:.2f}")
print(f"GST (18%)       : ₹{gst}")
print(f"Grand Total     : ₹{grand_total:.2f}\n")
print(f"Per Person      : ₹{cost_per_person:.2f}\n")

print("=" * 55)
