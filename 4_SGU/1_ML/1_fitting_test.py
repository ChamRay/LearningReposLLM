import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # 线性回归模型
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

# 1. 生成数据
X = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(X)+ np.random.uniform(low=-0.5,high=0.5,size=300).reshape(-1,1)
print(X.shape)
print(y.shape)

# 画出散点图，三个子图
fig, ax = plt.subplots(1,3,figsize=(15,4))
ax[0].scatter(X,y,c='r')
ax[1].scatter(X,y,c='y')
ax[2].scatter(X,y,c='b')
# plt.show()

# 2. 划分训练集和测试集
train_X,test_X,train_y,test_y = train_test_split(X,y,test_size=0.2,random_state=42)

# 3. 定义模型
model = LinearRegression()

# 一、欠拟合（直线）
x_train1 = train_X
x_test1 = test_X


# 4. 训练模型
model.fit(x_train1,train_y)

# 打印查看模型参数
print(model.coef_)
print(model.intercept_)

# 5. 预测结果，计算误差
y_pred1 = model.predict(x_test1)
test_loss1 = mean_squared_error(test_y,y_pred1)
train_loss1 = mean_squared_error(train_y,model.predict(x_train1))
# 画出拟合曲线，并写出训练误差和测试误差
ax[0].plot(X,model.predict(X),'r')
ax[0].text(-3,1,f"测试误差：{test_loss1:.4f}")
ax[0].text(-3,1.3,f"训练误差：{train_loss1:.4f}")
plt.rcParams['font.sans-serif'] = ['KaiTi', 'Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False
plt.show()


