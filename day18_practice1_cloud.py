aws_response = {
    "Reservations": [
        {
            "Instances": [
                {"InstanceId": "i-12345", "State": "running", "Type": "t2.micro"},
                {"InstanceId": "i-67890", "State": "stopped", "Type": "m5.large"},
                {"InstanceId": "i-abcde", "State": "running", "Type": "t2.micro"}
            ]
        }
    ]
}


target_list = aws_response["Reservations"][0]["Instances"]
for server in target_list:
    current_state = server["State"]  # Extract the state string
    current_id = server["InstanceId"] # Extract the ID string

    if current_state == "stopped":
        print(f"ALERT: Instance {current_id} is STOPPED.")