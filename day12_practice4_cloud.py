try:
    instance_name = input("Enter the instance name: ")
    if instance_name == "error":
        raise ValueError("Failed to launch instance.")
    else:
        print(f"Instance '{instance_name}' launched successfully.")
except ValueError as e:
    print(e)