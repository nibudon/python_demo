import re

s = 'Hello, Mr.Gumby : 2016/10/26  Hello,r.Gumby : 2016/10/26'

regex = "(?P<name>\w+\.\w+)"

regList = re.compile(regex).findall(s)
# 不加环视限定
print(regList)