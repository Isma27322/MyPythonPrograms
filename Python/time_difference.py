from datetime import datetime

def get_valid_date(prompt):
  """Prompts the user for a date in MM/DD/YYYY format and validates it."""
  while True:
    date_str = input(prompt)
    try:
      date = datetime.strptime(date_str, "%m/%d/%Y")
      return date
    except ValueError:
      print("Invalid date format. Please enter in MM/DD/YYYY format (e.g., 01/01/2023).")

def time_between_dates(start_date_str, end_date_str):
  """Calculates the time difference between two dates in various units."""

  # Convert strings to datetime objects
  start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
  end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

  # Calculate time difference in seconds
  total_seconds = (end_date - start_date).total_seconds()

  # Calculate time difference in other units
  days = int(total_seconds / 86400)
  months = days / 30.4375  # Average number of days in a month
  weeks = int(days / 7)
  years = days / 365
  percent_year = (days / 365) * 100
  minutes = int(total_seconds / 60)
  hours = int(minutes / 60)

  # Return results as a dictionary with commas for formatting
  return {
      "seconds": f"{int(total_seconds):,}",
      "days": f"{days:,}",
      "months": f"{months:.2f}",
      "weeks": f"{weeks:,}",
      "years": f"{years:.2f}",
      "percent_year": f"{percent_year:.2f}%",
      "minutes": f"{minutes:,}",
      "hours": f"{hours:,}"
  }

# Get valid start and end dates from the user
start_date_str = get_valid_date("Enter the start date in MM/DD/YYYY format: ")
end_date_str = get_valid_date("Enter the end date in MM/DD/YYYY format: ")

# Calculate time difference and print results
time_difference = time_between_dates(start_date_str, end_date_str)
print(f"Time difference between {start_date_str} and {end_date_str}:")
for key, value in time_difference.items():
  print(f"- {key}: {value}")
