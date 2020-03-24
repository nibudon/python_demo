def readTxt():
    f_path = r'C:\Users\Administrator\Desktop\test.txt'
    list = []
    with open(f_path, encoding="utf-8") as f:
        for line in f:
            list.append(line)
        return list

def writeTxt(list,f_path):
    # f_path = r'C:\Users\Administrator\Desktop\test2.txt'
    with open(f_path,'w', encoding="utf-8") as f:
        for line in list:
            f.write(line)

if __name__ == '__main__':
    list = readTxt()
    print(list[0])
    writeTxt(list,r'C:\Users\Administrator\Desktop\test2.txt')