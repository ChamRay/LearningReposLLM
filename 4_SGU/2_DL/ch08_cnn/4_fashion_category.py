import torch
import torch.nn as nn
import pandas as pd
import matplotlib.pyplot as plt

from torch.utils.data import TensorDataset,DataLoader

# 1. 加载数据
fashion_train = pd.read_csv('../data/fashion-mnist_train.csv')
fashion_test = pd.read_csv('../data/fashion-mnist_test.csv')
# 从数据中提取X和y，转成张量形式
x_train = fashion_train.iloc[:,:-1].values
x_train = torch.tensor(x_train,dtype=torch.float).reshape(-1,1,28,28)
y_train = fashion_train.iloc[:,0].values
y_train = torch.tensor(y_train,dtype=torch.int64)

x_test = fashion_test.iloc[:,:-1].values
x_test = torch.tensor(x_test,dtype=torch.float).reshape(-1,1,28,28)
y_test = fashion_test.iloc[:,0].values
y_test = torch.tensor(y_test,dtype=torch.int64)

# 显示图片和标签信息
# plt.imshow(x_train[12345,0,:,:],cmap='gray')
# plt.show()
# print(y_train[12345])

train_dataset = TensorDataset(x_train,y_train)
test_dataset = TensorDataset(x_test,y_test)

# 2. 创建模型
model = nn.Sequential(
    nn.Conv2d(1, 6, 5, stride=1, padding=2),
    nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),

    nn.Conv2d(6, 16, 5, stride=1, padding=0),
    nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),

    nn.Flatten(),

    nn.Linear(400, 120),
    nn.Sigmoid(),

    nn.Linear(120, 84),
    nn.Sigmoid(),

    nn.Linear(84, 10),
)

x = torch.rand(size=(1,1,28,28),dtype=torch.float)
for layer in model:
    x = layer(x)
    print(f"{layer.__class__.__name__:<12},output shape: {x.shape}")

# 模型训练和测试
def train_test(model,train_dataset,test_dataset,lr,epoch_num,batch_size,device=torch.device('mps')):
    # 参数初始化
    def init_weights(m):
        if type(m) == nn.Conv2d or type(m) == nn.Linear:
            nn.init.xavier_uniform_(m.weight)
    # 3.1 初始化
    model.apply(init_weights)
    model.to(device)
    # 定义损失函数
    loss = nn.CrossEntropyLoss()
    # 定义优化器
    optimizer = torch.optim.SGD(model.parameters(),lr=lr)
    # 3.2 训练过程
    for epoch in range(epoch_num):
        model.train()
        # 定义dataloader
        train_loader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
        running_loss = 0.0
        train_correct = 0
        # 按小批量循环迭代
        for batch_idx,(X,y) in enumerate(train_loader):
            X,y = X.to(device),y.to(device)
            # 3.2.1 前向传播
            output = model(X)
            # 3.2.2 计算损失
            loss_value = loss(output,y)
            # 3.2.3 反向传播
            loss_value.backward()
            # 3.2.4 更新参数
            optimizer.step()
            # 3.2.5 梯度清零
            optimizer.zero_grad()

            # 累计训练损失
            running_loss += loss_value.item() * X.shape[0]
            # 累加预测正确的数量
            pred = output.argmax(dim=1)
            train_correct += pred.eq(y).sum()
            # 模拟打印进度条
            print(f"\rEpoch:{epoch+1:0>2}[{'=' * int((batch_idx+1)/len(train_loader) * 50)}]",end='')
        this_train_loss = running_loss/len(train_dataset)
        this_train_acc = train_correct/len(test_dataset)


        # 验证过程
        model.eval()
        test_loader = DataLoader(test_dataset,batch_size=batch_size,shuffle=True)
        test_correct = 0
        with torch.no_grad():
            for X,y in test_loader:
                X,y = X.to(device),y.to(device)
                output = model(X)
                test_correct += output.argmax(dim=1).eq(y).sum()
        # 计算预测准确率
        this_test_loss = test_correct/len(test_dataset)
        print(f"train loss:{this_train_loss:.4f},train_acc:{this_train_acc:.4f},test_loss:{this_test_loss:.4f}")

device = torch.device('msp' if torch.backends.mps.is_available() else 'cpu')
# 定义超参数
lr = 0.9
epoch_num = 20
batch_size =256
train_test(model,train_dataset,test_dataset,lr,epoch_num,batch_size,device)

# 选取一个数据，进行测试对比
plt.imshow(x_test[666,0,:,:],cmap='gray')
plt.show()
print(y_test[666])
output = model(x_test[666].unsqueeze(0).to(device))
y_pred = output.argmax(dim=1).cpu().numpy()