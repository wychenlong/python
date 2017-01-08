#!/usr/bin/python3
import keyword

#print(keyword.kwlist)
# Python3 中有六个标准的数据类型 Number（数字）String（字符串）List（列表）Tuple（元组）Sets（集合）Dictionary（字典）
counter,miles,name = 100 ,1000.0 ,"runoob"
print(counter)
print(miles)
print(name)
print(name[0:-1])  # 输出第一个个到倒数第二个的所有字符

#del name             #删除引用
#print(name)

#name[0]='ss'         #字符串不可变
#print(name[0])
# 列表数据结构
list = ['abcd', 786 , 2.23, 'r', 70.2 ]
tinylist = [123, 'runoob']   #数据类型嵌套
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
list.insert(1,890)
print(list)
#元组
tuple = ( 'q', 7 , 5.23, 'run', 70.2)
tinytuple = (123, 'fg')
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

#Set集合
student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
print(student)   # 输出集合，重复的元素被自动去掉

#字典
tinydict = {'name': 'dsf','code':1, 'site': 'www.runoob.com'}
print (tinydict['name'])     # 输出键为 'name' 的值

print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("test1")
        break
    print("循环数据"+site)
else:
    print("没有循环数据!")
#迭代器
for it in iter(sites):
    print(it)

