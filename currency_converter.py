base_conversion_value = 0.013

# "123" -> string
# 123 -> INTEGER
# 1234.126 -> FLOAT


# take INR as Input
INR_value = float(input("Enter INR value :"))

# conversion
USD_value = INR_value * base_conversion_value

# print out the USD value
print("Converted USD VALUE is : ",USD_value)