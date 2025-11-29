import os
import shutil

# Ask the user for folders
source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")

# Create destination folder if it does not exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    # Check if file ends with .jpg (case-insensitive)
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)

        # Move file
        shutil.move(src_path, dst_path)
        print("Moved:", filename)

print("\nAll .jpg files have been moved successfully!")