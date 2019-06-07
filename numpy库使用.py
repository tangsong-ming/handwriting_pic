import numpy as np
#np.array([x,y,z],dtype=int)  从列表元组创建数组
np.arange(1,10,1)#range
np.linspace(1,10,10)#1-10 十等分
np.indices((4,5))#4行5列矩阵
np.random.rand(4,5)#随机数组4行5列
#np.ones((m,n),dtype=int) m行n列全是1 的数组
#np.empty((m,n),dtype=int) m行n列全是0 的数组
a=np.ones((4,5))
a.ndim#数组轴的个数 二维这里
a.shape#(4,5)
a.size#20
a.itemsize#每个元素的字节大小
a.flat#数组元素的迭代器
a.resize(4,4)#直接作用于当前数组
b=a.reshape(2,8)
a.flatten()#降维返回折叠后的一维数组
print(a.ravel())#返回一维数组的视图
#row begin with 0  column start with 1
#np.add(x1,x2,[,y])   y=x1+x2
#substract   multiply divide floor_divide
#np.negative(x,[,y])
#np.power    remainder  乘方 取余
#np.equal(x1,x2,[,y])    not_equal   y=x1==x2
'''
np.less(x1,x2,[,y]) y=x1<x2
less_equal   <=      
greater  >  tongli  >=
np.where(condition[x,y])  根据给出的条件判断输出是x还是y
'''
print(np.rint(1.6))#四舍五入的
