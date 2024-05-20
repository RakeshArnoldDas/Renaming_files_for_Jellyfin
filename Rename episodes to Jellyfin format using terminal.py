import os

def rename_files(folder_path, season_number):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Initialize episode number
    episode_number = 1
    
    # Iterate through each file in the folder
    for file_name in files:
        # Split the file name and extension
        name, extension = os.path.splitext(file_name)
        
        # Construct the new file name
        new_file_name = f"S{season_number:02d}E{episode_number:02d}{extension}"
        
        # Handle backslashes and double quotes in file names
        file_name = file_name.replace('"', '\\"')
        new_file_name = new_file_name.replace('"', '\\"')
        
        # Construct the full paths of the old and new files
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        
        # Increment episode number for the next file
        episode_number += 1

# Ask user for season number
season_number = int(input("Enter the season number: "))

# Provide the full path to the folder containing the files to be renamed
folder_path = input("Enter the full path to the folder containing the files: ").strip('"')

# Call the function to rename files in the folder
rename_files(folder_path, season_number)

print("Files renamed successfully.")
