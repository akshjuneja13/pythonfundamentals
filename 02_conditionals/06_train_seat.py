# Ticket info system for a railway
# Based on seat type, show its features

# Task:
# Input: "sleeper", "AC", "luxury", "general"
# Use match-case to display features
# Unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/luxury/general): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: Non-AC, economical, suitable for long journeys")
    case "ac":
        print("AC: Air-conditioned, comfortable, mid-range pricing")
    case "luxury":
        print("Luxury: Premium amenities, spacious seating")
    case "general":
        print("General: Basic seating, affordable, reserved for short journeys")
    case _:
        print("Invalid seat type")