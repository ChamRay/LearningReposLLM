import torch
import matplotlib.pyplot as plt

x = torch.linspace(5,-5,1000,requires_grad=True)
y = torch.tanh(x)

# 画图
fig, ax = plt.subplots(1,2,figsize=(12,4))
ax[0].plot(x.data,y.data,color="purple")
ax[0].set_title("sigmoid")
ax[0].axhline(y=-1,color='gray',alpha=0.5,linestyle='--',linewidth=1)
ax[0].axhline(y=1,color='gray',alpha=0.5,linestyle='--',linewidth=1)
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_position("zero")
ax[0].spines['left'].set_position("zero")
y.sum().backward()

ax[1].plot(x.data,x.grad,'purple')
ax[1].set_title("sigmoid gradient")
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_position("zero")
ax[1].spines['left'].set_position("zero")
# 调整坐标轴的位置


plt.show()
