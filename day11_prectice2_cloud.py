try:
    file_name = input("Enter the file name: ")
    if not file_name:
        raise ValueError("File name cannot be empty.")

except ValueError:
    print("Invalid input. Please enter a valid file name.")
else:
    print(f" Uploading {file_name} to S3 bucket...")
