import torch
import torch.nn as nn

# 自定义神经网络类
class Model(nn.Module):
    # 初始化
    def __init__(self):
        super().__init__()
        # 定义三个线性层
        self.linear1 = nn.Linear(3, 4)
        nn.init.xavier_normal(self.linear1.weight)
        self.linear2 = nn.Linear(4, 4)
        nn.init.kaiming_normal(self.linear2.weight)
        self.out = nn.Linear(4, 2)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.tanh(x)

        x = self.linear2(x)
        x = torch.relu(x)

        x = self.out(x)
        x = torch.softmax(x,dim=1)
        return x

# 测试
# 1. 定义输入数据
x = torch.randn(10,3)

# 2. 创建神经网络模型
model = Model()

# 3. 前向传播
output = model(x)
print("神经网络输出为：",output)

# 查看参数
params = model.parameters()
for param in params:
    print(param)

params = model.named_parameters()
for param in params:
    print(param)

param_dict = model.state_dict()
print(param_dict)


from torchsummary import summary
# 传入模型和输入维度
summary(model, input_size=(3,),batch_size=10,device='cpu')

'''
Param #：包含了权重和偏置的总数量
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Linear-1                    [10, 4]              16
            Linear-2                    [10, 4]              20
            Linear-3                    [10, 2]              10
================================================================
'''



