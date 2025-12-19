import re

text = "the comapany is going to launch a new product soon. the price is going to be around 1000 dollars.and revenue is expected to be around 1000000 dollars.and the company is expected to make a profit of around 500000 dollars."
numbers = re.findall(r"\d+", text)

print(numbers)