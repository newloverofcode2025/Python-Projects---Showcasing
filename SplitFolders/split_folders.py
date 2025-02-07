import os
import shutil

def organize_files(directory):
    """Organizes files into subfolders based on their extensions."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:]  # Get file extension
            if ext:
                folder_path = os.path.join(directory, ext.upper())
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_path}")

if __name__ == "__main__":
    directory = "files"
    print(f"Organizing files in {directory}...")
    organize_files(directory)