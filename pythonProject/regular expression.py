import re

#r = read or raw string
print(re.findall(r'[Pp]ython',"sunil is\n writing python \t is good"))

match = re.search(r'sunil', "sunil is working")
print(match)
print(match.start())
print(match.end())
print('Range',re.search(r'[a-zA-Z]',"SUNIL"))
print('Range',re.search(r'[S.N.L]',"SUNIL"))
print('Range',re.search(r'[S.*]',"SUNIL"))
print('not start with',re.search(r'[^a-z]',"sunil"))
print('search sunil',re.search(r'[a-z]{5}',"sunil"))

print(re.search(r'[\d]{2}',"today's date is 10/25/2023"))
print(re.findall(r'[\S]',"meline macline dsouza"))