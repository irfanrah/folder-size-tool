import os
import argparse
from datetime import datetime

def get_folder_size(folder_path):
    """Calculate the total size of all files in a folder."""
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                print(f"Error accessing file: {file_path}")
                continue
    return total_size

def format_size(size_in_bytes, size_type):
    """Convert bytes to the specified size type (MB or GB)."""
    if size_type.lower() == 'mb':
        return size_in_bytes / (1024 * 1024)
    elif size_type.lower() == 'gb':
        return size_in_bytes / (1024 * 1024 * 1024)
    return size_in_bytes

def print_tree_with_size(root, level=1, current_level=1, size_type="GB", output_file=None):
    """Recursively write directories in a tree format with their sizes to a file."""
    if current_level > level:
        return
    
    # Get folder size and format it
    folder_size = format_size(get_folder_size(root), size_type)
    line = "  " * (current_level - 1) + f"|- {os.path.basename(root)}/ ({folder_size:.2f} {size_type.upper()})\n"
    
    # Write to the file
    output_file.write(line)

    # Recurse into subdirectories
    for item in os.listdir(root):
        item_path = os.path.join(root, item)
        if os.path.isdir(item_path):
            print_tree_with_size(item_path, level, current_level + 1, size_type, output_file)

def main():
    parser = argparse.ArgumentParser(description="Display directory tree with folder sizes.")
    parser.add_argument("--path", type=str, default="./", help="Path to the root directory.")
    parser.add_argument("-l", "--level", type=int, default=3, help="Depth level of the directory tree.")
    parser.add_argument("-s", "--size_type", type=str, default="GB", choices=["MB", "GB"],
                        help="Size unit for displaying folder sizes (default is GB).")
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print("Invalid directory path")
        return
    
    # Generate file name with the current date
    date_str = datetime.now().strftime("%Y%m%d")
    output_filename = f"size_{date_str}.txt"
    
    # Open the output file and write the tree
    with open(output_filename, "w") as output_file:
        print_tree_with_size(args.path, args.level, size_type=args.size_type, output_file=output_file)

    print(f"Output saved to {output_filename}")

if __name__ == "__main__":
    main()
