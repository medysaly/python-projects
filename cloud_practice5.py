import re
phone = "1234567890 # secret number"
clean_phone = re.sub(r"#.*", "", phone )
print(clean_phone)  