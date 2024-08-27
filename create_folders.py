import os

# Define the base directory where the folder structure will be created
base_dir = "output"

# Define the folder structure as shown in the image
folder_structure = {
    "Authors": [
        "Most Relevant Authors",
        "Authors' Production over Time",
        "Lotka's Law",
        "Authors' Local Impact"
    ],
    "Affiliations": [
        "Most Relevant Affiliations",
        "Affiliations' Production over Time"
    ],
    "Countries": [
        "Corresponding Author's Countries",
        "Countries' Scientific Production",
        "Countries' Production over Time",
        "Most Cited Countries"
    ]
}

# Function to create folders based on the structure
def create_folder_structure(base_dir, structure):
    for main_folder, sub_folders in structure.items():
        main_folder_path = os.path.join(base_dir, main_folder)
        os.makedirs(main_folder_path, exist_ok=True)
        for sub_folder in sub_folders:
            sub_folder_path = os.path.join(main_folder_path, sub_folder)
            os.makedirs(sub_folder_path, exist_ok=True)

# Create the folder structure
create_folder_structure(base_dir, folder_structure)

print(f"Folder structure created in '{base_dir}'")
