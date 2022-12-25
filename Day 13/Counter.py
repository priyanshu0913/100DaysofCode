
from collections import Counter

# initializing string
test_str = input("Enter a string  : ")

# printing original string
print("The original string is : " + test_str)

# using collections.Counter() + max() to get
# Maximum frequency character in String
res = Counter(test_str)
res = max(res, key=res.get)

# printing result
print("The maximum of all characters is : " + str(res))
