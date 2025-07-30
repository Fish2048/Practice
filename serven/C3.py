
a=[1,2,3,4,5,6]

for i in range(10,0,-2): #
    #从10开始，每次减2，直到0
    print(i, end='|')  #end='|'表示输出后不换行
#输出10|8|6|4|2|

b=[1,2,3,4,5,6]
for i in range(0, len(b), 2):  #从0开始，每次加2，直到列表长度
    print(b[i], end='|')  #输出1|3|5|

c=b[0:len(b):2]  #切片，获取从0到列表长度，每隔2个元素
print(c)  #输出[1, 3, 5]

#类的定义和使用
#类是对象的蓝图，定义了对象的属性和方法
class class1:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Hello, {self.name}')

import p1     #导入serven.p1模块
print(p1.a)  #从serven/p1.py中导入a

