import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Lasso,Ridge # 线性回归模型
from sklearn.preprocessing import PolynomialFeatures # 构建多项式特征
from sklearn.model_selection import train_test_split # 划分训练集和测试集
from sklearn.metrics import mean_squared_error # 均方误差损失函数

'''
1. 生成数据
2. 划分训练集和测试集（验证集）
3. 定义模型（线性回归模型）
4. 训练模型
5. 预测结果，计算误差（损失）
'''
plt.rcParams['font.sans-serif'] = ['KaiTi', 'Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False
# 1. 生成数据
X = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(X)+ np.random.uniform(low=-0.5,high=0.5,size=300).reshape(-1,1)
print(X.shape)
print(y.shape)

# 画出散点图，三个子图
fig, ax = plt.subplots(2,3,figsize=(15,8))
ax[0,0].scatter(X,y,c='g')
ax[0,1].scatter(X,y,c='y')
ax[0,2].scatter(X,y,c='b')
# plt.show()

# 2. 划分训练集和测试集
train_X,test_X,train_y,test_y = train_test_split(X,y,test_size=0.2,random_state=42)

poly20 = PolynomialFeatures(degree=20)
x_train = poly20.fit_transform(train_X)
x_test = poly20.fit_transform(test_X)

# 一、不加正则化
# 3. 定义模型
model = LinearRegression()
# 4. 训练模型
model.fit(x_train,train_y)
# 5. 预测结果，计算误差
y_pred = model.predict(x_test)
test_loss = mean_squared_error(test_y,y_pred)
# 画出拟合曲线，并写出训练误差和测试误差
ax[0,0].plot(X,model.predict(poly20.fit_transform(X)),'r')
ax[0,0].text(-3,1,f"测试误差：{test_loss:.4f}")
# 画所有系数的直方图
ax[1,0].bar(np.arange(21),model.coef_.reshape(-1))

# 二 增加L1正则化项，Lasso回归
lasso = Lasso(alpha=0.01)
# 4. 训练模型
lasso.fit(x_train,train_y)
# 5. 预测结果，计算误差
y_pred = lasso.predict(x_test)
test_loss = mean_squared_error(test_y,y_pred)
# 画出拟合曲线，并写出训练误差和测试误差
ax[0,1].plot(X,lasso.predict(poly20.fit_transform(X)),'r')
ax[0,1].text(-3,1,f"测试误差：{test_loss:.4f}")
# 画所有系数的直方图
ax[1,1].bar(np.arange(21),lasso.coef_.reshape(-1))

# 三 增加L2正则化项，岭回归
ridge = Ridge(alpha=1)
# 4. 训练模型
ridge.fit(x_train,train_y)
# 5. 预测结果，计算误差
y_pred = ridge.predict(x_test)
test_loss = mean_squared_error(test_y,y_pred)
# 画出拟合曲线，并写出训练误差和测试误差
ax[0,2].plot(X,ridge.predict(poly20.fit_transform(X)),'r')
ax[0,2].text(-3,1,f"测试误差：{test_loss:.4f}")
# 画所有系数的直方图
ax[1,2].bar(np.arange(21),ridge.coef_.reshape(-1))

plt.show()


