

def lastIndexOf(s,k):
    lenth = len(s)
    result = ""
    for i in range(lenth):
        result = result + s[lenth - i - 1]
    return lenth - result.find(k) - 1

num = 12
# s = "nibudon,zyl,zrho"
s = "zrh-r-"
# print(s.split(","))
# print(s.startswith("nibu",0,4))
# print(s.endswith("zrh"))
# print(s.count("i"))
# print(s.capitalize())
# print(s.casefold())
# print("=======================")
# print(s.center(7,"-"))
# print(s.count("1"))
# print(s[0:3])
# print(s.find("r"))
# print(s.index("r"))
# tmpStr = s

start = s.find("r")
end = lastIndexOf(s,"r")
print(s[start:end + 1])

# in_str = input("输入：")
# print(type(in_str))