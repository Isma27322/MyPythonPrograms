import os

def find_and_open_videos(video_name, folder_path):
  """Recursively searches for videos with names containing the search term 
  and allows user selection."""
  videos = []  # List to store video paths

  for root, _, files in os.walk(folder_path):
    for file in files:
      if file.lower().endswith('.mp4') and video_name.lower() in file.lower():
        full_path = os.path.join(root, file)
        videos.append(full_path)

  # Check if any videos were found
  if not videos:
    print(f"No videos found in '{folder_path}' or its subfolders containing '{video_name}'.")
    return

  # List matching videos
  print("Found videos:")
  for i, video in enumerate(videos):
    print(f"{i+1}. {os.path.relpath(video, folder_path)}")  # Display relative path only

  # Get user selection
  while True:
    try:
      selection = int(input("Enter the number of the video to open (or 0 to cancel): "))
      if 0 <= selection <= len(videos):
        break
      else:
        print("Invalid selection. Please enter a number between 0 and", len(videos))
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Open selected video
  if selection > 0:
    full_path = videos[selection - 1]  # Access video path from the list
    if os.path.isfile(full_path):
      os.startfile(full_path)
      print(f"Opening video: {full_path}")
    else:
      print(f"Error: Video not found: {full_path}")  # Handle missing video
  else:
    print("Selection cancelled.")

# Specific folder path (replace with your actual path if different)
folder_path = "C:\\Users\\Manni\\Downloads\\Plex\\" 

# Get user input for video name (search term)
video_name = input("Enter video name (search term): ")

# Call the function to search and open videos
find_and_open_videos(video_name, folder_path)
