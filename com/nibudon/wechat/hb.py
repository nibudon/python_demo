import itchat
import pygame

'''声音提示'''

def voice ():
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()

'''监控群聊红包(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=True)
def getNoteGroup(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        voice()

'''监控个人红包(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=False)
def getNote(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        voice()

itchat.auto_login(hotReload=True)
itchat.run()