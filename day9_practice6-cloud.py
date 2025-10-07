def get_aws_service_cost(service_name):
    mock_costs = {
        "EC2": 120.50,
        "S3": 45.75,
        "RDS": 89.30,
        "Lambda": 15.20,
        "DynamoDB": 30.00
    }
    return mock_costs.get(service_name, 0.0)   

user_input = input("Enter AWS service name (e.g., EC2, S3, RDS, Lambda, DynamoDB): ") 
cost = get_aws_service_cost(user_input)
print(f"The estimated monthly cost for {user_input} is: ${cost:.2f}")