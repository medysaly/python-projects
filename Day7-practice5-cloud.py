aws_services = ["EC2", "S3", "Lambda", "RDS", "DynamoDB"]
for i in aws_services:
    if i == "S3":
        print("this is a storage service")
    print(i)
