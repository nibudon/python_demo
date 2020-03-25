from os import path

import speech_recognition as sr

# 语音转文字
def voice2Text(file_name):
    voice_file = path.join(path.dirname(path.realpath(__file__)), file_name)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(voice_file) as source:
        audio = r.record(source)
    try:
        content = r.recognize_google(audio, language='zh-CN')
        # print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))

    return content or '无法翻译'