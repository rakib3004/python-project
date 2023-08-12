import os
import shutil

def replace_spaces_with_hyphens(folder_path):
    for filename in os.listdir(folder_path):
        if " " in filename:
            new_filename = filename.replace(" ", "-")
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            shutil.move(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    target_folder = r"C:\Users\pc\Documents\Github\Tech-Edu-Assistant\doc\Pdf3\SPL2Slides"
    replace_spaces_with_hyphens(target_folder)
