#python的基本数据类型  Python3
#number：数字   整数int、小数float
print(1)
print(type(1))
print(type(-1))
print(type(1.111111))
print(type(1+1.1))
print(type(1+1))
print(type(1+1.0))
print(type(1*1))
print(type(1*1.0))
print(type(2/2))
print(type(2//2))
#2/2 float  1.0  除法，得到的是浮点数
#2//2 int  1    整除
print(1//2)
#10进制：0,1,2,3,4.....9,10
#2进制:0,1,10
#8进制:0,1......7,10
#16进制:0,1,2......9,A,B,C,D,E,F
#二进制
print(0b10)
print(0b11)
#八进制
print(0o10)
print(0o11)
#十六进制
print(0x10)
print(0x11)
#十进制
print(10)
print(11)
#转二进制
bin(10)
bin(0o7)
bin(0xE)
#转十进制
int(0b11)
int(0o77)
#转十六进制
hex(0o777)
#转八进制
oct(0b111)
oct(0x777)
#bool 布尔： 真 假
#complex 复数
print(True)
print(False)
#type函数查看数据类型
bool(0) #False
bool(1) #True 非0
bool('abc')
bool('') #False
bool([1,2,3]) #True 列表
bool([]) #False 空列表
bool({1,2,3})
bool({}) #空元组 False
bool(None) #false
print(26j) #复数
#str字符串
#单引号，双引号，多引号
print('hello world')
print(type('1'))
print("Let's go") #英文缩写
print(r'hello \n world')
print("hello"*3)
print("hello world"[0]) #输出第一个字符
print("hello world"[-1])
print("hello world"[0:4])
print("hello world"[0:5]) #截取字母的下一位
print("hello world"[0:-1])#-1代表步长
print("hello world"[6:11])
print("hello world"[6:]) #什么都不用输就是截取到最后 
#相同表达方式
print("hello world"[:-5]) 
print("hello world"[0:-5])
#负数在冒号前面的意义
print("------------")
print("hello world"[-5:])
print("hello world"[-4:])#负数在冒号前面的意义
print("hello world"[-1:])
print('---------列表------')
#组 列表 [] 可修改，哈希值会改变
print(type([1,2,3,4,5,6]))
print(['hello',1,"world",False])
print([1,2],[3,4],[True,1])
print(["死吻","弧光","舜华","幻舞"][-1:])
print(["死吻","弧光","舜华","幻舞"]+["精灵舞步","叶舞"]) #两个列表相加
A=["死吻","弧光","舜华","幻舞"]+["精灵舞步","叶舞"]
A.append("测试")
print(A)

#两个列表相乘
print(["死吻","弧光","舜华","幻舞"]*3)
print(['巴西','克罗地亚','墨西哥','喀麦隆'],[],[],[]) #映射到我们的python中
# 元组 ()不可修改，可作为dict的key，哈希值不会变
print("-------------")
print(1,2,3,4,5)
print(1,'-1',True)
print((1,2,3,4)[0])
print((1,2,3,4)[0:2])
print((1,2,3,4)+(5,6,7,8))
print((1,2,3,4)*3)
print(type((1,2,3,4)))
print(type((1)))  #()既表示元组，也表示运算符号，当只有一个元素时，会先计算出来再展示
print(type((1,))) #表示一个元组
print(type([1])) 

#str,list,tuple是序列
#序列共有的操作：1."hello"[0] [1,2,3][0] (1,2,3)[0]
# 切片：[1,2,3][0:3]  (1,2,3)[-1:]
# +，*
# 判断3是不是在列表[1,2,3,4,5,6]
# 
print("hello world"[0:8:2])
print(3 in [1,2,3,4,5,6,])
#知道序列长度
print(len((1,2,3,4,5,4)))
print(max((1,2,3,4,3,5,7))) #最小min

print(max(("hello world"))) #w
print(min(("hello world"))) 
print(min(("helloworld"))) #d

print(ord('w')) 
print(ord(' '))
print(ord('d'))

print('------set集合 无序-------')
#set{} 无序的，无法通过下标索引取元素
print(len({1,2,3,4,5,3})) #会去掉重复的元素
print(1 in (1,2,3,2,3,4))
print(1 not in (1,2,3,2,3,4))
print({1,2,3,4,5,6}-{3,4}) #求两个集合差集
print({1,2,3,4,5,6}&{3,4}) #求两个集合交集

print({1,2,3,4,5,6} | {3,4,7}) #求两个集合并集
print(type({})) #字典
print(type(set())) #集合
print(len(set()))

print('--------字典 dict---------')
#很多key和value，集合类型
print({'name':'lee','age':18,'sex':'女'})
#通过key访问值,字段不能有重复的key
print({'name':'lee','age':18,'sex':'女'}['name'])
print({'1':'lee',1:18,'sex':'女'}[1])
print({'name':'lee','name':18,'sex':'女'}['name'])#不能有重复的key
#value:str int float list set dict
#key:不可变的类型 列表不可以，但是元组可以
B=[1,2,4,5]
B.insert(2,"name")
print(B)



