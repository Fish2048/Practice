# if code:
#     pass
# else:
#     fail
a=True
if a:
    print("测试")
else:
    print('失败')

if True:
    pass  #占位符，什么都不做

if False:
    print('不会执行')
else:
    print('会执行')

if 1:
    print('会执行')
elif 0:
    print('不会执行')

#循环  递归合适
print('循环开始')
# while True:
#     print('循环')
#     break  #跳出循环
count = 1 #等于0的时候，是False
'''
LOL,打王者，直到打到王者
'''
while count <= 5:
    count += 1
    print(count)
else:
    print('循环结束')

'''
主要用来遍历/循环，序列或者集合、字典
'''
# for i in range(5):  #0-4
#     print(i)  #输出0-4
a = [['apple', 2, 3, 4, 'banana'],(1, 2, 3)]
for i in a: 
    #print(i)  #输出列表中的每个元素
    for j in i:  #如果是元组，遍历元组
        if y==3:
            print('找到3，跳出循环')
            break  #跳出内层循环
        print(j)  #输出元组中的每个元素
else:
    print('循环结束')

b=[1, 2, 3, 4, 5]
for i in b:
    if i == 3:
        print('找到3，跳出循环')
        continue  #跳出循环,不再执行后面的语句，所以只输出1,2，但是continue会跳出当前循环，继续执行后面的语句，打印出4,5
    print(i)  #输出1,2

