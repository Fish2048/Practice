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
#运算符 算数运算符
print('hello'+' '+'world')
print(5%2) #求余数
c=1
c=c+1
print(c)
#赋值运算符
c+=1
print(c)
b=3
a=2
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
#比较（关系）运算符 布尔类型
result=1==1
print(result)
a=1
b=2
print(a!=b)
print(1>1)
b=1
b+=b>=1
print(b) #int（True）=1
c='a'>'b'
print(c)
print(ord('a'))
d='abz'>'adc'  #一个一个字母比较
print(d)
#逻辑运算
print(True and True)
print('a' and 'b')
print([] or [1])
print(True or False)
print(True or True)
#or返回第一个
print ([1] or [2])
print([2] or [1])  
#and返回第二个
print([2] and [1])  
print([1] and [2])  

#成员运算符
res= a in [1,2,3,4,5]
print(res)


b='a'
print(b in {'c':1})
b='c' #成员运算符是针对key的
print(b in {'c':1})
b=1
print(b in {'c':1})

#身份运算符，两个取值相等，is返回True
a=1
b=1.0
print(a is b) #False
print(a==b)  
#关系运算符==是比较值相等
#身份运算符is比较内存地址

a=1
b=1
print(a is b)
print(id(a))
print(id(b))

a=[1,2,3]
b=[2,1,3]
print(a==b)
print(a is b)

c=(1,2,3)
d=(2,1,3)
print(c==d)
print(c is d)

e={1,2,3}
f={2,1,3}
print(e==f)
print(e is f)