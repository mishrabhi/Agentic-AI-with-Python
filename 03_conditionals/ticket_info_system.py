# You are building a ticket info system for a railway app
# Based on the seat type, show its feature
# Task:
# Input: 'sleeper', 'AC', 'general', 'luxury'
# Match using match-case
# Unknown -> Show invalid seat type

seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()
match seat_type:
    case "sleeper":
        print(f"Sleeper - No AC, but beds are available")
    case "ac":
        print(f"AC - Air conditioned")
    case 'general':
        print(f"General, these are cheapest option, no reservation required")
    case 'luxury':
        print(f"Premium seats with meals")
    case _:
        print("invalid seat type")