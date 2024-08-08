import os
import sys

def create_directory_and_files(base_name):
    # set directory and files name
    directory = base_name
    files = [f'{base_name}_go.md', f'{base_name}_cpp.md', f'{base_name}_py.md', f'README.md']

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")

    for file_name in files:
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write('')  
            print(f"File '{file_name}' created in '{directory}'.")
        else:
            print(f"File '{file_name}' already exists in '{directory}'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python create_files.py <base_name>")
        sys.exit(1)

    base_name = sys.argv[1]
    create_directory_and_files(base_name)
