import kagglehub
import os
import shutil as sh




# ==========================================
# DOWNLOAD DATA & CREATE FOLDER (IF NOT EXIST)
# ==========================================

# Download latest version
path = kagglehub.dataset_download("blastchar/telco-customer-churn")

# Get the parent directory path (outside 'src')
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))

# Define the 'data' folder path in the parent directory
data_dir = os.path.join(parent_dir, 'data')

# Create the 'data' folder if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)  # Create folder if it doesn't exist

    print(f"Folder created: {data_dir}")

    for file in os.listdir(path):
        source_path = os.path.join(path, file)  # Source path of the file
        destination_path = os.path.join(data_dir, file)  # Destination path in the 'data' folder
        sh.move(source_path, destination_path)  # Move file to 'data' folder

    print(f"Files moved to {data_dir}")
else:
    print(f"The folder already exists: {data_dir}")


# ==========================================
# EDA
# ==========================================

