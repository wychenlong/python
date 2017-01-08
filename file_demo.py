#!/usr/bin/python3
"""
 文件操作，读写文件
"""
fname = input("请输入文件名:")
def writeFile():
    try:
        fobj = open(fname,"wb+")
        content = bytes("test write file content","UTF-8")
        #写二进制文件
        fobj.write(content)
        fobj.flush()
    except IOError as e:
        print("file write error: {0}".format(e))
    else:
        print('write file success')

def read_file():
    try:
        fileObj = open(fname,"r")
    except IOError as e:
        print("file read error: {0}".format(e))
    else:
        for eachLine in fileObj:
            print("读取文件内容："+eachLine)
        fileObj.close()
writeFile()
read_file()