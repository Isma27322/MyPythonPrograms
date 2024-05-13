import os

def create_file(directory, filename, content=""):
  """Creates a new file with the specified name and optional content in a separate directory.

  Args:
      directory: The path to the directory where the file should be created.
      filename: The name of the file to create.
      content (str, optional): The content to write to the file. Defaults to "".
  """
  # Combine directory and filename to get the full path
  full_path = os.path.join(directory, filename)

  try:
    with open(full_path, "w") as file:
      file.write(content)
    print(f"File '{full_path}' created successfully!")
  except FileExistsError:
    print(f"Error: File '{full_path}' already exists.")

# Example usage
directory = "./StuffForKeeping/StuffForKeeping"  # Replace with your desired directory name
filename = "new_data.txt"
content = "This is some data for the new file."

# Create the directory if it doesn't exist (optional)
os.makedirs(directory, exist_ok=True)  # Creates directory structure if needed

create_file(directory, filename, content)
