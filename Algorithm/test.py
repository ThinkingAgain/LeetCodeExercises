import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据，pd.read_csv默认生成DataFrame对象，需将其转换成Series对象
d11 = pd.read_csv('Double11f.csv', encoding='utf-8')

plt.plot(d11['year'],d11['salevolume'],'r^',label='2009年至2018年双11全天销售额')

plt.title('淘宝2009年至2018年历年双11销售额',color='blue',size=20)
plt.xlabel('年份',size=16)
plt.ylabel('双11全天销售额',size=16)

# X坐标，将str类型的数据转换为datetime.date类型的数据，作为x坐标
#d11['iYear'] = [int(sv) for sv in d11['年份']]
#d11['iSalesVolume'] = [float(sv) for sv in d11['全天总交易额(亿元)']]
'''
model = LinearRegression()
model.fit(d11[['year']], d11['salevolume'])

years = [[2019], [2020]]
years = []
for year in range(12):
    years.append([2009+year])

salesVolume = model.predict(years)

plt.plot(years, salesVolume, 'g-')

'''
# 验证集
X_test = d11[['year']]
y_test = d11['salevolume']

years = np.linspace(2009, 2021, 13) # 设计x轴一系列点作为画图的x点集
print('years',years)
quadratic_featurizer = PolynomialFeatures(degree=2) # 实例化一个二次多项式特征实例
X_train_quadratic = quadratic_featurizer.fit_transform(d11[['year']]) # 用二次多项式对样本X值做变换
xx_quadratic = quadratic_featurizer.transform(years.reshape(years.shape[0], 1)) # 把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
regressor_quadratic = LinearRegression() # 创建一个线性回归实例
regressor_quadratic.fit(X_train_quadratic, d11['salevolume']) # 以多项式变换后的x值为输入，代入线性回归模型做训练
plt.plot(years, regressor_quadratic.predict(xx_quadratic), 'b-',label='二次多项式') # 用训练好的模型作图

print('coef:',regressor_quadratic.coef_, ' intercept：',regressor_quadratic.intercept_)
print('SaleVolume:',regressor_quadratic.predict(xx_quadratic)[-3:])
#print ('一元线性回归 r-squared', model.score(d11[['year']], d11['salevolume']))
X_test_quadratic = quadratic_featurizer.transform(d11[['year']])
print ('二次回归     r-squared', regressor_quadratic.score(X_test_quadratic, d11['salevolume']))

# 绘制三次回归曲线
cubic_featurizer = PolynomialFeatures(degree=3)
X_train_cubic = cubic_featurizer.fit_transform(d11[['year']])
regressor_cubic = LinearRegression()
regressor_cubic.fit(X_train_cubic, d11['salevolume'])
xx_cubic = cubic_featurizer.transform(years.reshape(years.shape[0], 1))
plt.plot(years, regressor_cubic.predict(xx_cubic), 'y-',label='三次多项式')


X_test_cubic = cubic_featurizer.transform(X_test)
print ('三次回归     r-squared', regressor_cubic.score(X_test_cubic, y_test))
print('SaleVolume:',regressor_cubic.predict(xx_cubic)[-3:])
print('预测2019年淘宝双11当天销售额:',regressor_quadratic.predict(xx_quadratic)[-3:-2][0])
print('预测2020年淘宝双11当天销售额:',regressor_quadratic.predict(xx_quadratic)[-2:-1][0])
print('预测2021年淘宝双11当天销售额:',regressor_quadratic.predict(xx_quadratic)[-1:][0])
print('预测2019年淘宝双11当天销售额:',regressor_cubic.predict(xx_cubic)[-3:-2][0])
print('预测2020年淘宝双11当天销售额:',regressor_cubic.predict(xx_cubic)[-2:-1][0])
print('预测2021年淘宝双11当天销售额:',regressor_cubic.predict(xx_cubic)[-1:][0])


plt.legend(loc='upper left')
plt.show()
