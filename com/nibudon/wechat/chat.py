import time
from time import sleep

import itchat

'''1、登录后给文件助手发消息'''
# itchat.auto_login()
# itchat.send('Hello, filehelper', toUserName='filehelper')

'''2、登录后自动回复收到的消息'''
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
#
# itchat.auto_login()
# itchat.run()

'''3、识别消息类型，并自动回复，包括群消息'''
# import itchat, time
# from itchat.content import *
#
# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     msg.user.send('%s: %s' % (msg.type, msg.text))
#
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
#
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
#
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
#
# itchat.auto_login(True)
# itchat.run(True)

'''4、定时发送消息，消息内容为txt文件中内容'''
def readTxt():
    f_path = r'msg.txt'
    list = []
    with open(f_path, encoding="utf-8") as f:
        for line in f:
            list.append(line)
        return list

# itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.auto_login(hotReload=True)
print("登录成功")
msg = readTxt()[0]
sendTime = '2020-03-25 13:45:00'
localtime = time.strptime(sendTime,"%Y-%m-%d %H:%M:%S")
# 获取指定时间戳，时间戳 x 1000 = 毫秒数
tt = time.mktime(localtime)
users=itchat.search_friends("倪卟懂")
userName= users[0]['UserName']
hasSend = False;
while True:
    now = time.time()
    itchat.auto_login(hotReload=True)
    if now >= tt and now < tt + 10:
        if not hasSend:
            print(now)
            itchat.send(msg, toUserName=userName)
            hasSend = True
            print("消息发送成功")
    sleep(1)



# 获取所有群的相关信息， name根据群名称获取指定群信息
# search_chatrooms 获取通讯录中群聊列表 update=True 会获取实时有信息的群
# myroom = itchat.get_chatrooms(update=True)

'''5、定时发送指定消息到指定群'''

def readTxt2():
    f_path = r'msg.txt'
    list = []
    with open(f_path, encoding="utf-8") as f:
        for line in f:
            list.append(line)
        return list

# itchat.auto_login()
# itchat.auto_login(enableCmdQR=1)


# itchat.auto_login(enableCmdQR=2)
# print("登录成功")
# msg = readTxt2()[0]
# groupName = '随便'
# sendTime = '2020-03-25 21:50:00'
# localtime = time.strptime(sendTime,"%Y-%m-%d %H:%M:%S")
# # 获取指定时间戳，时间戳 x 1000 = 毫秒数
# tt = time.mktime(localtime)
# hasSend = False;
# myroom = itchat.search_chatrooms(name=groupName)
# for room in myroom:
#     # NickName 获取群名称
#     if room['NickName'] == groupName:
#         while True:
#             now = time.time()
#             itchat.auto_login(hotReload=True)
#             if now >= tt and now < tt + 10:
#                 if not hasSend:
#                     # UserName 获取群UUID 根据ID发送信息
#                     username = room['UserName']
#                     # send_msg 发送信息 参数：信息内容，uid
#                     itchat.send_msg(msg, username)
#                     hasSend = True
#                     print("消息发送成功")
#             sleep(1)
#     else:
#         print('No groups found')