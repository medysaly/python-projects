ebs_response = {
    "ResponseMetadata": {"RequestId": "abc-123-xyz"},
    "Volumes": [
        {"VolumeId": "vol-001", "State": "in-use", "Size": 100},
        {"VolumeId": "vol-002", "State": "available", "Size": 50},
        {"VolumeId": "vol-003", "State": "available", "Size": 20},
        {"VolumeId": "vol-004", "State": "in-use", "Size": 500}
    ]
}

target_list = ebs_response["Volumes"]
for volume in target_list:
    state = volume["State"]
    volume_id = volume["VolumeId"]

    if state == "available":
        print(f"ALERT: Unsed Volume found: {volume_id}")