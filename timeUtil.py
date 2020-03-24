import time

def getCurrentTime1():
    result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return result

def getCurrentTime2():
    # 获取当前时间戳，时间戳 x 1000 = 毫秒数
    timeMilions = time.time()
    t = time.localtime(timeMilions)
    result = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return result

def getTimeMilions(t):
    localtime = time.strptime(t,"%Y-%m-%d %H:%M:%S")
    # 获取指定时间戳，时间戳 x 1000 = 毫秒数
    tt = time.mktime(localtime)
    ttt = time.localtime(tt)
    result = time.strftime("%Y/%m/%d %H:%M:%S",ttt)
    return result

def getDateList(t,days):
    result = []
    if not t:
        t = time.time()
    t = time.strptime(t,"%Y-%m-%d %H:%M:%S")
    localetime = time.mktime(t)
    for i in range(days):
        tmp = localetime - 60*60*24*i
        tmpTT = time.localtime(tmp)
        result.append(time.strftime("%Y%m%d",tmpTT))
    result.reverse()
    return result

def getDateList2(days):
    result = []
    localtime = time.time()
    for i in range(days):
        tmp = localtime - 60*60*24*i
        tmpTT = time.localtime(tmp)
        result.append(time.strftime("%Y%m%d",tmpTT))
    result.reverse()
    return result

def list_test():
    list1 = [1,2,3,4,5,6]
    print(list1)
    list1.reverse()
    print(list1)

if __name__ == '__main__':
    print("获取当前时间1："+getCurrentTime1())
    print("获取当前时间2："+getCurrentTime2())
    print("指定时间："+getTimeMilions("2020-02-26 21:00:00"))
    print(getDateList("2020-02-25 09:00:00",30))
    print(getDateList2(30))