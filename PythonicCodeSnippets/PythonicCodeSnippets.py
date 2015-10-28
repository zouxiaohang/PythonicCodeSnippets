# -*- coding:utf-8 -*-

#(1)获得正负无穷的float值
'''当涉及 > 和 < 运算时, 所有数都比-inf大, 所有数都比+inf小'''
maxFloat = float('inf')
minFloat = float('-inf')

#(2)交换两个变量值
a, b = b, a

#(3)字符串列表的连接
strList = ["Python", "is", "good"]  
res =  ' '.join(strList) #Python is good 
res = ''.join(strList) #Pythonisgood




if __name__ == "__main__":
    print("main")