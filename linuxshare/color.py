from webcolors import name_to_hex

def get_hex_from_name(color_name):
  try:
    hex_code = name_to_hex(color_name).upper()  # Convert to uppercase for consistent format
    # Check if "#" exists and remove it before prepending "0x"
    if hex_code.startswith("#"):
      hex_code = hex_code[1:]  # Remove leading "#" if present
    return f"0x{hex_code}"  # Prepend "0x" without the "#"
  except ValueError:
    return None

# Get color name input from the user, remove spaces with loop
color_name = input("Enter a color name: ").lower()
color_name_no_spaces = ""

# Loop to remove all spaces (including multiple)
for char in color_name:
  if char != " ":
    color_name_no_spaces += char

hex_color = get_hex_from_name(color_name_no_spaces)

if hex_color:
  print(f"Hex code (without '#') for '{color_name}': {hex_color}")
else:
  print(f"Color '{color_name}' not found in the database.")
