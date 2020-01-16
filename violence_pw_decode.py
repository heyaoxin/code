#-*-coding:utf-8-*-
import zipfile

#生成1-999999的数字密码表, 要是有别的密码类型，对密码表改造一下就可以了，也可以上网下载某些类型的密码字典
def code_dic():
    with open('./code_dictionary.txt','w') as f:
        for i in range(1000000):
            pw = str(i)+'\n'
            f.write(pw)
    pass

#遍历密码表进行暴力破解
def encode():
    zf = zipfile.ZipFile('haha.zip')
    with open('./code_dictionary.txt', 'r') as f:
        password_list = f.read().split()#文件转换成密码列表
        for i in range(len(password_list)):
            password = password_list[i]
            try:
                zf.extractall(pwd=str.encode(password))#带密码解压
                print('破解成功，密码是:',password)
                break
            except:
                continue
    pass

def main():
    #code_dic()
    encode()
    pass
if __name__ == '__main__':
    main()