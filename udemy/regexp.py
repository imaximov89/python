import re

pattern = re.compile('this')
str = 'search inside this text please'

res = pattern.search(str)
print(res.group())
