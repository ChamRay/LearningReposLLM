import torch
import torch.nn as nn

from torchsummary import summary

# 1. 定义数据
x = torch.randn(10,3)

# 2. 构建模型
model = nn.Sequential(
    nn.Linear(3,4),
    nn.Tanh(),
    nn.Linear(4,4),
    nn.ReLU(),
    nn.Linear(4,2),
    nn.Softmax(dim=1),
)

def init_weights(layer):
    if type(layer) == nn.Linear:
        nn.init.xavier_uniform_(layer.weight)
        nn.init.constant_(layer.bias, 0.1)

# 3. 参数初始化
model.apply(init_weights)

# 4. 前向传播
output = model(x)

summary(model, input_size=(3,),batch_size=10)