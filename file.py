import os

def rename_files(directory, prefix='', suffix='', replace_name=None):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        for file_name in files:
            # Get the file's full path
            old_file_path = os.path.join(directory, file_name)
            
            # Skip directories
            if os.path.isdir(old_file_path):
                continue
            
            # Extract file extension
            name, ext = os.path.splitext(file_name)
            
            # Generate new file name
            if replace_name:
                new_name = f"{replace_name}{ext}"
            else:
                new_name = f"{prefix}{name}{suffix}{ext}"
            
            # Construct new file path
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_name}")
        
        print("Renaming complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
#directory = "path/to/your/directory"
#rename_files(directory, prefix="new_", suffix="_v1")
