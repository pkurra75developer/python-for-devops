import re

str1 = "How many times I have to say you should not do it. Did you hear me?"

pattern = r"you"

res = re.search(pattern, str1)
# you should never write if res == True: or if res is True: 
# Below is the right way of using bool in if condition. you can also say if not res: for negation

if res :
    print("your search pattern found", res.group())
else:
    print("didn't find your search pattern")

# Difference between re.search and re.match in Python?

# re.match() searches for matches from the beginning of a string while re.search() searches for matches anywhere in the string.

# re.match attempts to match a pattern at the beginning of the string. re.search attempts to match the pattern throughout the string until it finds a match

# Example:

import re

claim = 'People love Python.'

print(re.search(r'Python', claim).group())
# => Python

print(re.match(r'Python', claim))
# => None

print(re.search(r'People', claim).group())
# => People

print(re.match(r'People', claim).group())
# => People
