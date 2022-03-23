str = "X-DSPAM-Confidence:0.8475"

colonindex = str.find(":")+1
new_str = str[colonindex:]
new_str = float(new_str)

print(new_str)
print(type(new_str))