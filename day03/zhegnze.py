import re

# p = re.compile(r'[A-Z]')
# p=re.compile(r'([0-9]*)')
# p=re.compile(r'\D')#非数字
p=re.compile(r'e*')
print(p.findall('he3l_4elo'))
