def months_to_decimal(months, days):
  """Converts months and days to a decimal number of months (rounded to 100 places).

  Args:
      months: Number of whole months.
      days: Number of days.

  Returns:
      The decimal equivalent of the months and days (rounded to 100 places).
  """

  # Approximate days as a decimal of a month (assuming 30 days/month)
  decimal_days = round(days / 30, 100)

  # Combine whole months and decimal months
  total_months = months + decimal_days

  return round(total_months, 100)

# Get user input
months = int(input("Enter the number of months: "))
days = int(input("Enter the number of days: "))

decimal_months = months_to_decimal(months, days)

print(f"{months} months and {days} days is equivalent to approximately {decimal_months:.100f} months (rounded to 100 places).")
