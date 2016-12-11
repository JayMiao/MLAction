import re

p = re.compile(r'\d+')
match = p.search('one1two2three3four4')
print match.group()

### output ###
# ['1', '2', '3', '4']