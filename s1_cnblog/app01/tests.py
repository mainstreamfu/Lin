from django.test import TestCase

# Create your tests here.
# import datetime
from datetime import datetime
from datetime import timedelta

# print(datetime.datetime.now())
#
# date_obj = datetime.datetime.now()
# x=date_obj.strptime('2017年9月30日星期六8时42分24秒','%Y年%m月%d日星期六%H时%M分%S秒')
# print(type(date_obj))
# print(date_obj.year)
# print(type(date_obj.month))
# print(x)
# print()
#
#
# dt=datetime.datetime.now()
# n=dt.strftime('%Y-%m-%d %H:%M:%S')
# print(n,type(n))


# now = datetime.now()
# delta = now - datetime(2017,6,27,10)
# print(now,type(now))
# print(now.date(),type(now.date()))
# print(now.time(),type(now.time()))
# print(delta,type(delta))
# print(delta.days,type(delta.days))


# from datetime import datetime
# dt=datetime.now()
# n=dt.strftime('%m/%d/%Y %H:%M:%S %p')
# print(n)
# n=dt.strftime('%Y年%m月%d日星期%w %H时%M分%S秒')
# print(n)
# n=dt.strftime('%A,%B, %d,%Y')
# print(n)
# n=dt.strftime('%B %d,%Y')
# print(n)
# n=dt.strftime('今天是%Y年%m月%d日')
# print(n)
# n=dt.strftime('今天是这周的第%w天')
# print(n)
# n=dt.strftime('今天是今年的第%j天')
# print(n)
# n=dt.strftime('今天是今年的第%W周')
# print(n)
# n=dt.strftime('今天是当月的第%d天')
# print(n)


# import calendar
#
# cal = calendar.month(2016, 1)
# print ("以下输出2016年1月份的日历:")
# print (cal)

# import time
#
# localtime = time.localtime(time.time())
# print ("本地时间为 :", localtime)
#
# localtime = time.asctime( time.localtime(time.time()) )
# print ("本地时间为 :", localtime)
#
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
#
#
# print("*"*120)
# import time
# （1）当前时间戳
# time.time()
# one = time.time()
# # print(one)
# #
# # # （2）时间戳 → 时间元组，默认为当前时间
# # # time.localtime()  括号中放时间戳
# # two = time.localtime(time.time())
# # print(two)
# # print(time.localtime(123456))
# #
# # # （3）时间戳 → 可视化时间
# # # time.ctime(时间戳)，默认为当前时间
# # three = time.ctime(1562467704.0623)
# # print(three)
# #
# # # （4）时间元组 → 时间戳
# # # 1538271871
# # four = time.mktime((2019, 7, 7, 9, 44, 31, 6, 273, 0))
# # print(four)
# #
# # # （5）时间元组 → 可视化时间
# # # time.asctime(时间元组)，默认为当前时间
# #
# # five = time.asctime((2019, 7, 7, 10, 48, 24, 6, 273, 0))
# # five1 = time.asctime(time.localtime(1562467704.0623))
# # print(five,five1)
# #
# # # （6）时间元组 → 可视化时间（定制）
# # # time.strftime(要转换成的格式，时间元组)
# # six = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # print(six)
# #
# # # （7）可视化时间（定制） → 时间元祖
# # # time.strptime(时间字符串，时间格式)
# # print("时间元祖:",time.strptime('2019-7-7 11:32:23', '%Y-%m-%d %H:%M:%S'))
# #
# # # （8）将格式字符串转换为时间戳
# # eight = "Sun Jul  7 10:48:24 2019"
# # print (time.mktime(time.strptime(eight,"%a %b %d %H:%M:%S %Y")))
# #
# #
# # # 字符类型的时间
# # tss1 = '2013-10-10 23:40:00'
# # # 转为时间数组
# # timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# # print(timeArray)
# # # timeArray可以调用tm_year等
# # print(timeArray.tm_year)  # 2013
# # # 转为时间戳
# # timeStamp = int(time.mktime(timeArray))
# # print(timeStamp) # 1381419600

# from datetime import datetime
# S=datetime.strptime('2019/07/07','%Y/%m/%d')
# print(S,type(S))
# S=datetime.strptime('2019年7月7日星期日','%Y年%m月%d日星期日')
# print(S,type(S))
# S=datetime.strptime('2019年7月7日星期日8时42分24秒','%Y年%m月%d日星期日%H时%M分%S秒')
# print(S,type(S))
# S=datetime.strptime('7/7/2019','%m/%d/%Y')
# print(S,type(S))
# S=datetime.strptime('7/7/2019 8:42:50','%m/%d/%Y %H:%M:%S')
# print(S,type(S))

# dt=datetime.now()
# s=dt.strftime('%m/%d/%Y %H:%M:%S %p')
# print(s,type(s))
# s=dt.strftime('%A,%B %d,%Y')
# print(s,type(s))
# week = dt.strftime('%w')
# print(week,type(week))
# if week == "1":
#     week="一"
# elif week == "2":
#     week="二"
#
#
#
#
# txt =('%s年%s月%s日星期%s %s时%s分%s秒'%(dt.strftime('%Y')\
# ,dt.strftime('%m'),dt.strftime('%d'),week,dt.strftime('%H'),dt.strftime('%M'),dt.strftime('%S')))
# print(txt)
# s=dt.strftime('%B %d,%Y')
# print(s,type(s))

# dt=datetime.now()
#
#
# def week(dt):
#     if type(dt) is datetime:
#         ags = dt.strftime('%w')
#         int_ret=int(ags)
#         l = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]
#         # return print(l[int_ret])
#         ret = l[int_ret]
#     else:
#         ret = "数据类型错误"
#     return print(ret)
# # week(dt)


# dt=datetime.now()
# s=dt.strftime('%m/%d/%Y %H:%M:%S %p')
# print(s,type(s))


# sum = sum(range(0,101))
# print(sum)


# num = 1
# def fun():
#     global a
#     a = 10
#     print(a)
# fun()
# print(a)

# dic = {"name":"Diy","age":11}
# del dic["name"]
# print(dic)                      #结果：{'age': 11}

# dic2 = {"name":"James"}
# dic.update(dic2)
# print(dic)                      #结果：{'age': 11, 'name': 'James'}

# list = [1,1,2,2,3,3,4,4,5,5]
# demo = set(list)
# print(demo)
#
# demo1 = [i for i in demo]
# print(demo1)

# def this_fun(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# this_fun(0,1,2,3,index1=11,index2=22)

# print(range(100))
#
# a=range(100)
#
# print(a)

# list = [1,2,3,4,5]
# #
# # def fun(x):
# #     return x**2
# #
# # rse = map(fun,list)
# # l = [i for i in rse if i>10]
# # print(l)
# #
# # k = rse(1)
# # print(k)

# import random
# import numpy as np
#
# res1 = random.randint(10,20)
# res2 = np.random.randn(5)
# res3 = random.random()
# print(res1)
# print(res2)
# print(res3)

# import datetime
#
# datetime.date:"年月日"
#
# datetime.time:"时分秒"
#
# datetime.datetime:"年月日 时分秒"
#
# datetime.timedelta:"构建时间对象"


# Python中可变数据类型列表  字典

# Python中不可变数据类型数字 元祖  字符串


# d = {1:{"xxx":[1,2,3]},2:{"xxx":[4,5,6]},3:{"xxx":[7,8,9]}}
#
# d[1]["xxx"].append(d[2]["xxx"])
#
# d[2]["xxx"].append(d[3]["xxx"])
# print(d)

comment_list = [
    {"id": 1, "content": "111", "Pid": None},
    {"id": 2, "content": "222", "Pid": None},
    {"id": 3, "content": "333", "Pid": None},
    {"id": 4, "content": "444", "Pid": 1},
    {"id": 5, "content": "555", "Pid": 1},
    {"id": 6, "content": "666", "Pid": 4},
    {"id": 7, "content": "777", "Pid": 3},
    {"id": 8, "content": "888", "Pid": 7},
    {"id": 9, "content": "999", "Pid": None},
]

# for obj in comment_list:
#     # print(obj["Pid"])
#     i = obj["Pid"]
#     if i == None:
#         obj["children_list"] = []
#         for j in comment_list:
#             pid = j["Pid"]
#             if pid == obj["id"]:
#                 obj["children_list"].append(j)
#             else:
#                 pass
# print(comment_list)

# ret=[
#     {"id":1,"content":"111","Pid":None,"children_list":[]},
#     {"id":2,"content":"222","Pid":None},
#     {"id":3,"content":"333","Pid":None},
#     {"id":9,"content":"999","Pid":None},
# ]

# 字典的生成试
# d = {"1":111,"2":222}
#
# dic = {v:k for k,v in d.items()}
#
# print(dic)
# ******一旦某个数据引用了一个可变数据类型，可变数据类型发生变化，该数据跟着发生变化
# for obj in comment_list:
#     id = obj["id"]
#     obj["children_list"] = []
#     for j in comment_list:
#         pid = j["Pid"]
#         if pid == id:
#             obj["children_list"].append(j)
#         else:
#             pass
# print(comment_list)


for obj in comment_list:
    obj["children_list"] = []
# print(comment_list)

ret = []

for obj in comment_list:
    pid = obj["Pid"]
    if pid:
        for i in comment_list:
            if i["id"] == pid:
                i["children_list"].append(obj)
    else:
        ret.append(obj)

print(ret)

[{'id': 1, 'content': '111', 'Pid': None, 'children_list':
    [{'id': 4, 'content': '444', 'Pid': 1, 'children_list':
        [{'id': 6, 'content': '666', 'Pid': 4, 'children_list': []}]},
     {'id': 5, 'content': '555', 'Pid': 1, 'children_list': []}]},
 {'id': 2, 'content': '222', 'Pid': None, 'children_list': []},
 {'id': 3, 'content': '333', 'Pid': None, 'children_list':
     [{'id': 7, 'content': '777', 'Pid': 3, 'children_list':
         [{'id': 8, 'content': '888', 'Pid': 7, 'children_list': []}]}]},
 {'id': 4, 'content': '444', 'Pid': 1, 'children_list':
     [{'id': 6, 'content': '666', 'Pid': 4, 'children_list': []}]},
 {'id': 5, 'content': '555', 'Pid': 1, 'children_list': []},
 {'id': 6, 'content': '666', 'Pid': 4, 'children_list': []},
 {'id': 7, 'content': '777', 'Pid': 3, 'children_list':
     [{'id': 8, 'content': '888', 'Pid': 7, 'children_list': []}]},
 {'id': 8, 'content': '888', 'Pid': 7, 'children_list': []},
 {'id': 9, 'content': '999', 'Pid': None, 'children_list': []}]

[{'id': 1, 'content': '111', 'Pid': None, 'children_list':
    [{'id': 4, 'content': '444', 'Pid': 1, 'children_list':
        [{'id': 6, 'content': '666', 'Pid': 4, 'children_list': []}]},
     {'id': 5, 'content': '555', 'Pid': 1,'children_list': []}]},
 {'id': 2, 'content': '222', 'Pid': None, 'children_list': []},
 {'id': 3, 'content': '333', 'Pid': None,'children_list':
     [{'id': 7, 'content': '777', 'Pid': 3,'children_list':
         [{'id': 8, 'content': '888','Pid': 7,'children_list': []}]}]},
 {'id': 9, 'content': '999', 'Pid': None, 'children_list': []}]
