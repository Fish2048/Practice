#变量赋值 =
A=[1,2,3,4,5,6]
B=[1,2,3]
print(A*3+B+A)
skill=['新月打击','苍白之瀑']  #命名可读性要强，用简单简介的英文单词表示一个变量
#2025.7.7
#变量字母，数字，下划线，首字母不能是数字，系统关键字，不能用在变量中，保留关键字，如and，if，import等
type=3
print(type) #虽然可以，但不推荐，容易出现错误
#变量名区分大小写
a=2
A=4
print(A)
print(a)
a=1
b=a
a=3
print(b)
a=[0,1,2,3,4,5]
b=a
a[0]='1'
print(b)
#引用类型 list set dict 可改变
#值类型 int str tuple 不可变
a='hello'
a=a +'python'
print(a)
#a[0]='1'   a是字符串，无法改变
print(a[0])
a=[1,2,3]
print(hex(id(a)))
a[0]='2'
print(hex(id(a)))
a.append(4)
print(a)
a=(1,2,3,[1,2,4])
print(a[3][2])
a=(1,2,3,[1,2,['a','b','c']])
print(a[3][2][2])
#运算符
print('hello'+' '+'world')
