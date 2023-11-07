str1 = "The textbooks are good for reading"
str1 = str1.replace("good","great")

str2 = "arn:123456:role/james"
str2 = str2.split("/")

str3 = "  I am padded with a transparent gown. You can see me. But not feel it     "
str_stripped = str3.strip()

## Looks like there is NO substring function in Python" The way to find is as below
str4 = "Welcome to the beautiful world of computers"
str5 = "Bountiful"

if str5 in str4:
   print("beautiful is found")
else:
   print("beautiful is NOT found")

print(str1)
print(str2)
print(str2[0])
print(str2[1])
print("------------------------")
print(len(str3))
print(str_stripped)
print(len(str_stripped))



