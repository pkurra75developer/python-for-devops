import re
str1 = "Welcome to the world of good leaders"

pattern = r"good"

replacement = "bad"

newstring = re.sub(pattern, replacement, str1)

print(newstring)


