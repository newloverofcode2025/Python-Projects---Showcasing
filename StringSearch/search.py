import os

def search_string_in_files(directory, search_string):
    """Searches for a string in all files within a directory."""
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Checking file: {file_path}")  # Debugging information
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"Content of {file_path}: {content[:100]}...")  # Print first 100 characters
                    if search_string in content:
                        results.append(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return results

if __name__ == "__main__":
    directory = input("Enter the directory path to search: ")
    search_string = input("Enter the string to search: ")

    found_files = search_string_in_files(directory, search_string)

    if found_files:
        print(f"\nFound '{search_string}' in the following files:")
        for file in found_files:
            print(file)
    else:
        print(f"\nNo files found containing '{search_string}'.")