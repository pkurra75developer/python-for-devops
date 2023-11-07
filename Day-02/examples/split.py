# returns a list of resulting substrings
import re
str1 = "apple, banana, orange, grapes"

pattern = r","

newstring = re.split(pattern, str1)

print(newstring)


