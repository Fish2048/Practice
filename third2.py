#表达式是运算符和操作数所构成的序列
#操作数同级，从左向右依次（左结合） 
#赋值运算符= 会变成右结合
a=1
b=2
c=3
print(a or b and c)  #and的优先级比or高
mood=False
#if后可以跟表达式
if mood:
    print('go to left')
    print('back away')
else:
    print('go to right')

#账号密码
#constant 常量
'''
一段小程序，模拟登录
'''
USERNAME='admin'
PASSWORD='123456'

account=input('请输入账号：')
user_password=input('请输入密码：')
if account == USERNAME and user_password == PASSWORD:
    print('登录成功') #四个空格缩进
else:
    print('账号或密码错误，请重新输入')