# Advanced data types: datetime, time, calendar, timedelta, arrow
import arrow
from collections import namedtuple

# Current UTC time using arrow
brewing_time = arrow.utcnow()
print(f"Current UTC time: {brewing_time}")

# Convert to another timezone
london_time = brewing_time.to("Europe/London")
print(f"London time: {london_time}")

# Namedtuple example
ChaiProfile = namedtuple("ChaiProfile", ["flavor", "sugar"])

# Create an instance
chai = ChaiProfile(flavor="ginger", sugar=2)

print(f"Chai flavor: {chai.flavor}")
print(f"Sugar level: {chai.sugar}")
print(f"Full chai profile: {chai}")