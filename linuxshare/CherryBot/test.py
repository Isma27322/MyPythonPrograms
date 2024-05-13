role_names = []
role_emojis = []
has_data = False  # Flag to track if data was found

with open('ReactionRoles.txt', 'r') as file:
  # Read all lines at once (check if any lines exist)
  lines = file.readlines()
  if not lines:
    print("File is empty.")
  else:
    # Find the first non-empty line (assuming headers are at the beginning)
    start_line = 0
    for line in lines:
      line = line.strip()  # Remove leading/trailing whitespace
      if line:
        has_data = True  # Set flag if any line is found (excluding headers)
        break
      start_line += 1

    # Iterate through lines starting from the first non-empty line
    for line in lines[start_line:]:
      line = line.strip()

      # Add lines with emojis (assuming "<a:" format) directly to emojis
      if line.startswith("<a:") or line.startswith("<:"):
        role_emojis.append(line)  # Append the entire line (including "<a:")
      else:
        # Add non-emoji lines as role names
        role_names.append(line)

# Print the results (if there's data)
if has_data:
  print("Role Names:", role_names)
  print("Role Emojis:", role_emojis)