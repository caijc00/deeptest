'''
Created on 2018年1月9日

@author: fajin.zhang
'''
import os,random

# 随机生成100个10至1000之间的数
# b = random.uniform(10, 1000)
a = []
for x in range(0,100):
    a.append(random.uniform(10, 1000))
#print(a)

# 实现排序，内部函数，冒泡
# list.sort(a)
def mysort():
    for x in range(0,100):
        for y in range(0,99):
            if a[y] < a[y+1]:
                m = a[y]
                a[y] = a[y+1]
                a[y+1] = m

if __name__ == '__main__':
    mysort()
    print (a)