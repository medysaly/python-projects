cloud_provider = input("Enter your favorite cloud provider: ").strip().upper()

if cloud_provider == "AWS":
    print(f"You said: {cloud_provider} ")
    print("AWS is a great cloud provider")

elif cloud_provider == "Azure":
    print(f"You said:{cloud_provider} ")
    print("Azure is a great cloud provider")
elif cloud_provider == "GCP":
    print(f"You said: {cloud_provider} ")
    print("GCP is a great cloud provider")
else:
    print(f"You said:{cloud_provider} ")
    print(f"{cloud_provider} is also a great cloud provider")