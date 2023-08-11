import os

def generate_folder_paths_txt(root_directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(root_directory):
            for dir_name in dirs:
                folder_path = os.path.join(root, dir_name)
                f.write(f"{folder_path}\n")

if __name__ == "__main__":
    root_directory = "/path/to/parent/folder"
    output_file = "folder_paths.txt"
    generate_folder_paths_txt(root_directory, output_file)