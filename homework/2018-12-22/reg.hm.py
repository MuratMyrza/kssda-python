import re

string = '&quot; Python Exercises &quot;'
print(string)

res = re.sub(r'\s+', '', string)
print(res)