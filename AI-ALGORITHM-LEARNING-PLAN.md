# 🎯 全栈AI算法工程师 - 详细学习计划

## 📊 学习时间概览

| 时间段 | 时长 | 备注 |
|--------|------|------|
| 工作日 | 1小时/天 × 5天 | 周一至周五 |
| 周末 | 2小时/天 × 2天 | 周六、周日 |
| **每周总计** | **9小时** | |

**总学习周期**: 约14-16个月 (62-70周)

---

## 📅 阶段一：机器学习基础 (第1-10周)

### 📚 学习资源
- 吴恩达《Machine Learning Specialization》(Coursera)
- 周志华《机器学习》(西瓜书)
- scikit-learn官方文档

---

### Week 1: Python基础与数据处理

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | NumPy基础 | 观看教程：数组创建、索引、切片、基本运算 |
| 周二 | 1h | NumPy进阶 | 广播机制、线性代数运算、随机数生成 |
| 周三 | 1h | Pandas基础 | Series与DataFrame、数据读取、基本操作 |
| 周四 | 1h | Pandas进阶 | 数据清洗、合并、分组聚合、时间序列 |
| 周五 | 1h | Matplotlib基础 | 折线图、柱状图、散点图、子图绘制 |
| 周六 | 2h | 数据可视化实战 | 练习：用Matplotlib绘制10种图表 |
| 周日 | 2h | 综合练习 | 完成Kaggle Titanic数据集探索性分析 |

---

### Week 2: 监督学习 - 线性模型

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 线性回归原理 | 吴恩达课程L1.1-L1.4：代价函数、梯度下降 |
| 周二 | 1h | 线性回归实战 | scikit-learn实现Boston房价预测 |
| 周三 | 1h | 多元线性回归 | 多变量、特征缩放、正规方程 |
| 周四 | 1h | 逻辑回归原理 | 吴恩达课程L2.1-L2.4：Sigmoid函数、决策边界 |
| 周五 | 1h | 逻辑回归实战 | scikit-learn实现鸢尾花分类 |
| 周六 | 2h | 正则化 | L1/L2正则化原理与实现 |
| 周日 | 2h | 正则化实战 | Ridge和Lasso回归对比实验 |

---

### Week 3: 监督学习 - 树模型

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 决策树原理 | 信息增益、基尼系数、剪枝策略 |
| 周二 | 1h | 决策树实战 | DecisionTreeClassifier实现 |
| 周三 | 1h | 随机森林原理 | Bagging思想、特征采样、OOB估计 |
| 周四 | 1h | 随机森林实战 | RandomForestClassifier调参 |
| 周五 | 1h | GBDT原理 | 梯度提升思想、残差拟合 |
| 周六 | 2h | XGBoost原理 | XGBoost算法详解、目标函数 |
| 周日 | 2h | XGBoost实战 | Kaggle房价预测竞赛入门 |

---

### Week 4: 监督学习 - SVM

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | SVM原理 | 最大间隔、支持向量 |
| 周二 | 1h | 核函数 | 线性核、多项式核、RBF核 |
| 周三 | 1h | SVM实战 | SVC实现手写数字识别 |
| 周四 | 1h | SVM调参 | C和gamma参数调优 |
| 周五 | 1h | KNN原理 | 距离度量、K值选择、KD树 |
| 周六 | 2h | KNN实战 | KNN分类器实现与优化 |
| 周日 | 2h | 监督学习综合 | 对比线性模型/树模型/SVM/KNN |

---

### Week 5: 无监督学习

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | K-means原理 | 算法流程、收敛性、K值选择(肘部法则) |
| 周二 | 1h | K-means实战 | 聚类客户细分项目 |
| 周三 | 1h | 其他聚类算法 | DBSCAN、层次聚类、高斯混合模型 |
| 周四 | 1h | PCA原理 | 降维思想、特征值分解、SVD |
| 周五 | 1h | PCA实战 | 数据可视化降维、特征压缩 |
| 周六 | 2h | 异常检测 | Isolation Forest、Local Outlier Factor |
| 周日 | 2h | 无监督学习综合 | 聚类+降维综合项目 |

---

### Week 6: 模型评估与选择

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 分类指标 | 准确率、精确率、召回率、F1、AUC-ROC |
| 周二 | 1h | 回归指标 | MAE、MSE、RMSE、R² |
| 周三 | 1h | 交叉验证 | K折交叉验证、分层采样 |
| 周四 | 1h | 模型选择 | 偏差-方差权衡、过拟合/欠拟合 |
| 周五 | 1h | 超参数调优 | 网格搜索、随机搜索、贝叶斯优化 |
| 周六 | 2h | Pipeline | sklearn Pipeline、特征工程链 |
| 周日 | 2h | 综合实战 | 完整ML项目：数据→特征→模型→评估 |

---

### Week 7: 特征工程

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 特征缩放 | 标准化、归一化、RobustScaler |
| 周二 | 1h | 编码技术 | One-Hot、Label Encoding、Target Encoding |
| 周三 | 1h | 特征构造 | 多项式特征、交互特征、日期特征 |
| 周四 | 1h | 特征选择 | 过滤法、包裹法、嵌入法 |
| 周五 | 1h | 缺失值处理 | 均值/中位数填充、插值、模型预测填充 |
| 周六 | 2h | 特征工程实战 | Kaggle竞赛特征工程实战 |
| 周日 | 2h | 项目实战 | 信用评分卡项目 |

---

### Week 8: 集成学习进阶

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | Bagging原理 | Bootstrap聚合、并行集成 |
| 周二 | 1h | Boosting原理 | 序列集成、AdaBoost |
| 周三 | 1h | GBDT进阶 | 损失函数设计、正则化技巧 |
| 周四 | 1h | XGBoost进阶 | 特征重要性、早停法、自定义目标 |
| 周五 | 1h | LightGBM | 直方图算法、GOSS、EFB |
| 周六 | 2h | LightGBM实战 | LightGBM竞赛实战 |
| 周日 | 2h | CatBoost | Ordered Boosting、类别特征处理 |

---

### Week 9-10: 机器学习项目实战

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| Week 9 周一 | 1h | 项目选题 | 选择Kaggle竞赛或真实数据集 |
| Week 9 周二 | 1h | 数据探索 | EDA、数据清洗、分布分析 |
| Week 9 周三 | 1h | 特征工程 | 特征构造与选择 |
| Week 9 周四 | 1h | 模型训练 | 多模型对比、超参调优 |
| Week 9 周五 | 1h | 模型融合 | Stacking、Blending |
| Week 9 周六 | 2h | 结果分析 | 错误分析、模型解释 |
| Week 9 周日 | 2h | 报告撰写 | 项目报告、代码整理 |
| Week 10 周一 | 1h | 模型优化 | 特征筛选、模型精调 |
| Week 10 周二 | 1h | 模型优化 | 继续优化 |
| Week 10 周三 | 1h | 结果提交 | Kaggle提交、排名更新 |
| Week 10 周四 | 1h | 总结复盘 | 项目复盘、经验总结 |
| Week 10 周五 | 1h | 笔记整理 | ML知识体系整理 |
| Week 10 周六 | 2h | 面试准备 | ML常见面试题整理 |
| Week 10 周日 | 2h | 查漏补缺 | 薄弱环节加强 |

---

## 📅 阶段二：深度学习巩固 (第11-18周)

### 📚 学习资源
- 李宏毅《深度学习》
- PyTorch官方教程
- Stanford cs231n (CNN部分)

---

### Week 11: 神经网络基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 感知机与MLP | 神经元模型、多层感知机原理 |
| 周二 | 1h | 前向传播 | 激活函数(ReLU, Sigmoid, Tanh)、输出层 |
| 周三 | 1h | 反向传播 | 链式法则、梯度计算、计算图 |
| 周四 | 1h | PyTorch基础 | 张量、自动求导、nn.Module |
| 周五 | 1h | PyTorch实战 | 手写数字识别(全连接网络) |
| 周六 | 2h | 优化器 | SGD、Momentum、Adam原理与对比 |
| 周日 | 2h | 优化器实战 | 不同优化器训练对比实验 |

---

### Week 12: CNN基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 卷积运算 | 卷积核、步长、填充、输出尺寸计算 |
| 周二 | 1h | CNN架构 | 池化层、BatchNorm、经典网络结构 |
| 周三 | 1h | LeNet/AlexNet | 经典CNN网络详解 |
| 周四 | 1h | VGG/GoogLeNet | 深度网络、Inception模块 |
| 周五 | 1h | ResNet原理 | 残差连接、恒等映射 |
| 周六 | 2h | PyTorch CNN | 实现简单CNN图像分类 |
| 周日 | 2h | CNN实战 | CIFAR-10图像分类项目 |

---

### Week 13: CNN进阶

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 数据增强 | 随机翻转、旋转、裁剪、颜色变换 |
| 周二 | 1h | 正则化技术 | Dropout、DropPath、Label Smoothing |
| 周三 | 1h | 学习率调度 | Warmup、CosineAnnealing、OneCycleLR |
| 周四 | 1h | 迁移学习 | ImageNet预训练、微调策略 |
| 周五 | 1h | 迁移学习实战 | ResNet迁移学习花卉分类 |
| 周六 | 2h | 轻量级模型 | MobileNet、ShuffleNet、EfficientNet |
| 周日 | 2h | 模型压缩 | 知识蒸馏、模型剪枝概念 |

---

### Week 14: RNN与序列模型

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | RNN原理 | 循环神经网络、隐藏状态、时间展开 |
| 周二 | 1h | RNN问题 | 梯度消失/爆炸、长期依赖问题 |
| 周三 | 1h | LSTM原理 | 遗忘门、输入门、输出门、细胞状态 |
| 周四 | 1h | GRU原理 | 更新门、重置门、与LSTM对比 |
| 周五 | 1h | PyTorch RNN | nn.RNN/nn.LSTM/nn.GRU使用 |
| 周六 | 2h | 序列预测实战 | 时间序列预测(股票/天气) |
| 周日 | 2h | 文本分类实战 | IMDB情感分析(RNN/LSTM) |

---

### Week 15: PyTorch进阶

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 自定义Dataset | 数据加载、DataLoader、数据增强 |
| 周二 | 1h | 训练循环 | 完整训练流程、验证、早停 |
| 周三 | 1h | GPU训练 | .to(device)、多GPU、混合精度 |
| 周四 | 1h | 模型保存/加载 | state_dict、检查点、断点续训 |
| 周五 | 1h | TensorBoard | 可视化训练过程、模型图 |
| 周六 | 2h | 训练技巧 | 梯度裁剪、权重初始化、诊断 |
| 周日 | 2h | 项目模板 | 构建可复用的训练框架 |

---

### Week 16: 目标检测基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 目标检测概述 | 任务定义、评价指标(mAP)、数据集 |
| 周二 | 1h | R-CNN系列 | R-CNN、Fast R-CNN、Faster R-CNN |
| 周三 | 1h | YOLO系列 | YOLOv1-v3原理演进 |
| 周四 | 1h | YOLO实战 | Ultralytics YOLOv8使用 |
| 周五 | 1h | 锚框机制 | Anchor设计、正负样本匹配 |
| 周六 | 2h | 目标检测实战 | 自定义数据集训练检测模型 |
| 周日 | 2h | NMS与后处理 | 非极大值抑制、检测结果优化 |

---

### Week 17: 图像分割基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 分割任务概述 | 语义分割、实例分割、全景分割 |
| 周二 | 1h | FCN原理 | 全卷积网络、转置卷积 |
| 周三 | 1h | U-Net原理 | 编码器-解码器、跳跃连接 |
| 周四 | 1h | U-Net实战 | 医学图像分割项目 |
| 周五 | 1h | DeepLab系列 | 空洞卷积、ASPP模块 |
| 周六 | 2h | 分割评估指标 | IoU、Dice系数、像素精度 |
| 周日 | 2h | 分割实战 | 人像分割/道路分割项目 |

---

### Week 18: 深度学习项目实战

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 项目规划 | 选择CV/NLP项目、制定计划 |
| 周二 | 1h | 数据准备 | 数据收集、清洗、增强 |
| 周三 | 1h | 模型设计 | 选择架构、设计实验 |
| 周四 | 1h | 训练调优 | 训练循环、超参调优 |
| 周五 | 1h | 结果分析 | 错误分析、可视化 |
| 周六 | 2h | 模型优化 | 进一步优化、集成 |
| 周日 | 2h | 项目总结 | 文档整理、代码review |

---

## 📅 阶段三：NLP核心 (第19-30周)

### 📚 学习资源
- Stanford cs224n
- Jay Alammar《The Illustrated Transformer》
- Hugging Face课程
- 李宏毅NLP课程

---

### Week 19: NLP基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | NLP概述 | NLP任务分类、挑战、应用场景 |
| 周二 | 1h | 文本预处理 | 分词、词干化、词形还原、停用词 |
| 周三 | 1h | 中文分词 | jieba、pkuseg、分词方法 |
| 周四 | 1h | 文本表示 | BoW、TF-IDF、N-gram |
| 周五 | 1h | Word2Vec原理 | CBOW、Skip-gram、负采样 |
| 周六 | 2h | 词向量实战 | 训练Word2Vec、可视化 |
| 周日 | 2h | 词向量应用 | 词相似度、类比任务 |

---

### Week 20: 词向量进阶

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | GloVe原理 | 共现矩阵、全局统计 |
| 周二 | 1h | FastText原理 | 子词信息、OOV处理 |
| 周三 | 1h | 词向量评估 | 词汇邻接、类比任务评估 |
| 周四 | 1h | 预训练词向量 | 加载和使用预训练模型 |
| 周五 | 1h | 词向量应用实战 | 文本分类(传统ML方法) |
| 周六 | 2h | 文本特征工程 | 基于词向量的特征构造 |
| 周日 | 2h | 情感分析实战 | 商品评论情感分析 |

---

### Week 21: Seq2Seq与Attention

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | Seq2Seq原理 | 编码器-解码器架构 |
| 周二 | 1h | 注意力机制 | Bahdanau Attention、Luong Attention |
| 周三 | 1h | 注意力可视化 | 注意力权重分析 |
| 周四 | 1h | 机器翻译基础 | 数据处理、评估指标(BLEU) |
| 周五 | 1h | Seq2Seq实战 | 简单机器翻译项目 |
| 周六 | 2h | Beam Search | 集束搜索解码策略 |
| 周日 | 2h | 注意力进阶 | 自注意力、多头注意力 |

---

### Week 22: Transformer架构

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | Transformer概述 | "Attention is All You Need"论文解读 |
| 周二 | 1h | 自注意力机制 | Q/K/V计算、缩放点积注意力 |
| 周三 | 1h | 多头注意力 | 多头拼接、位置编码 |
| 周四 | 1h | Transformer编码器 | 层归一化、残差连接、FFN |
| 周五 | 1h | Transformer解码器 | 掩码注意力、自回归生成 |
| 周六 | 2h | Transformer实现 | PyTorch实现Transformer |
| 周日 | 2h | Transformer调试 | 调试和理解模型行为 |

---

### Week 23: BERT基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | BERT概述 | 预训练-微调范式 |
| 周二 | 1h | BERT架构 | Embedding、Transformer Encoder |
| 周三 | 1h | 预训练任务 | MLM、NSP任务详解 |
| 周四 | 1h | Hugging Face入门 | transformers库安装、Pipeline |
| 周五 | 1h | BERT微调实战 | 文本分类任务微调BERT |
| 周六 | 2h | BERT变体 | RoBERTa、ALBERT、DistilBERT |
| 周日 | 2h | 模型评估 | 在不同数据集上评估BERT |

---

### Week 24: BERT应用

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 命名实体识别(NER) | 任务定义、BIO标注 |
| 周二 | 1h | NER实战 | BERT做NER任务 |
| 周三 | 1h | 关系抽取 | 实体关系识别任务 |
| 周四 | 1h | 问答系统 | 抽取式问答(SQuAD) |
| 周五 | 1h | 问答系统实战 | BERT做阅读理解 |
| 周六 | 2h | 文本相似度 | 语义相似度、文本匹配 |
| 周日 | 2h | 多标签分类 | 文本多标签分类实战 |

---

### Week 25: GPT系列

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | GPT-1原理 | 单向语言模型、生成式预训练 |
| 周二 | 1h | GPT-2原理 | 零样本学习、文本生成 |
| 周三 | 1h | GPT-3原理 | 少样本学习、In-Context Learning |
| 周四 | 1h | 文本生成实战 | GPT-2文本生成 |
| 周五 | 1h | 生成策略 | 贪心、Top-k、Top-p采样、Temperature |
| 周六 | 2h | 对话系统 | 开放域对话、检索增强 |
| 周日 | 2h | 代码生成 | GPT模型在代码生成中的应用 |

---

### Week 26: 文本生成进阶

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 条件生成 | 属性控制、风格迁移 |
| 周二 | 1h | 文本摘要 | 抽取式、生成式摘要 |
| 周三 | 1h | 文本摘要实战 | BART/T5做摘要任务 |
| 周四 | 1h | 机器翻译进阶 | 现代NMT系统、多语言模型 |
| 周五 | 1h | T5模型 | Text-to-Text框架 |
| 周六 | 2h | 多任务学习 | T5多任务实战 |
| 周日 | 2h | 提示工程 | Prompt Engineering基础 |

---

### Week 27: 模型压缩与加速

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 知识蒸馏 | 教师-学生框架、蒸馏损失 |
| 周二 | 1h | 蒸馏实战 | DistilBERT蒸馏实践 |
| 周三 | 1h | 模型剪枝 | 非结构化/结构化剪枝 |
| 周四 | 1h | 量化技术 | INT8/FP16量化、动态量化 |
| 周五 | 1h | ONNX导出 | 模型格式转换、ONNX Runtime |
| 周六 | 2h | 推理优化 | 批处理、KV Cache、Flash Attention |
| 周日 | 2h | 部署实战 | FastAPI部署BERT模型 |

---

### Week 28: NLP项目实战(1)

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 项目选题 | 文本分类/NER/问答系统选题 |
| 周二 | 1h | 数据准备 | 数据收集、清洗、标注 |
| 周三 | 1h | 基线模型 | 快速建立基线 |
| 周四 | 1h | 模型选择 | BERT/RoBERTa选择 |
| 周五 | 1h | 训练优化 | 学习率、Batch Size调优 |
| 周六 | 2h | 错误分析 | 分析模型失败案例 |
| 周日 | 2h | 模型改进 | 数据增强、模型集成 |

---

### Week 29: NLP项目实战(2)

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 模型优化 | 继续优化模型 |
| 周二 | 1h | 模型优化 | 超参精调 |
| 周三 | 1h | 结果分析 | 详细结果分析 |
| 周四 | 1h | 可视化 | 注意力可视化、错误案例分析 |
| 周五 | 1h | 文档撰写 | 项目文档整理 |
| 周六 | 2h | 代码整理 | 代码规范化、注释 |
| 周日 | 2h | 项目总结 | 复盘总结、经验提炼 |

---

### Week 30: NLP总结与复习

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 知识梳理 | NLP知识体系整理 |
| 周二 | 1h | 模型对比 | BERT/GPT/T5对比总结 |
| 周三 | 1h | 面试准备 | NLP面试题整理 |
| 周四 | 1h | 面试准备 | 模型原理问答准备 |
| 周五 | 1h | 论文阅读 | 重要NLP论文精读 |
| 周六 | 2h | 查漏补缺 | 薄弱环节加强 |
| 周日 | 2h | 阶段总结 | NLP阶段学习总结 |

---

## 📅 阶段四：计算机视觉 (第31-42周)

### 📚 学习资源
- Stanford cs231n
- Ultralytics YOLOv8教程
- Detectron2教程
- Hugging Face Diffusers

---

### Week 31: CV基础复习

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | CNN复习 | 卷积、池化、经典架构 |
| 周二 | 1h | 图像预处理 | 归一化、增强、数据加载 |
| 周三 | 1h | 图像分类实战 | PyTorch图像分类项目 |
| 周四 | 1h | 迁移学习 | ImageNet预训练模型使用 |
| 周五 | 1h | 模型评估 | 混淆矩阵、分类报告 |
| 周六 | 2h | 数据增强进阶 | Albumentations库使用 |
| 周日 | 2h | 训练技巧 | 学习率调度、早停、正则化 |

---

### Week 32: 目标检测基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 检测任务概述 | 任务定义、挑战、数据集 |
| 周二 | 1h | 检测指标 | IoU、mAP、FPS |
| 周三 | 1h | Anchor机制 | 锚框设计、正负样本分配 |
| 周四 | 1h | NMS原理 | 非极大值抑制、Soft-NMS |
| 周五 | 1h | 两阶段检测 | Faster R-CNN原理 |
| 周六 | 2h | 单阶段检测 | YOLO系列演进 |
| 周日 | 2h | Anchor-Free | FCOS、CenterNet |

---

### Week 33: YOLO实战

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | YOLOv8安装 | Ultralytics安装、环境配置 |
| 周二 | 1h | 数据准备 | COCO格式、自定义数据集 |
| 周三 | 1h | 模型训练 | YOLOv8训练自定义数据 |
| 周四 | 1h | 模型评估 | 验证集评估、指标分析 |
| 周五 | 1h | 模型推理 | 单张/批量推理、视频检测 |
| 周六 | 2h | 模型导出 | ONNX/TensorRT导出 |
| 周日 | 2h | 部署实战 | FastAPI部署检测服务 |

---

### Week 34: 高级检测

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | DETR原理 | 端到端检测、二部图匹配 |
| 周二 | 1h | Deformable DETR | 可变形注意力机制 |
| 周三 | 1h | 实例分割 | Mask R-CNN原理 |
| 周四 | 1h | 全景分割 | Panoptic FPN |
| 周五 | 1h | 关键点检测 | 人体姿态估计 |
| 周六 | 2h | 多目标跟踪 | DeepSORT、ByteTrack |
| 周日 | 2h | 检测综合实战 | 完整检测项目 |

---

### Week 35: 图像分割

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 分割概述 | 语义/实例/全景分割 |
| 周二 | 1h | FCN原理 | 全卷积网络、转置卷积 |
| 周三 | 1h | U-Net原理 | 编码器-解码器、跳跃连接 |
| 周四 | 1h | U-Net实战 | 医学图像分割 |
| 周五 | 1h | DeepLab系列 | 空洞卷积、ASPP |
| 周六 | 2h | 分割评估 | IoU、Dice、像素精度 |
| 周日 | 2h | 分割实战 | 人像分割/道路分割 |

---

### Week 36: 生成模型基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | GAN原理 | 生成器-判别器对抗训练 |
| 周二 | 1h | GAN训练技巧 | 模式坍塌、训练不稳定 |
| 周三 | 1h | DCGAN原理 | 深度卷积GAN、架构设计 |
| 周四 | 1h | DCGAN实战 | 人脸生成项目 |
| 周五 | 1h | WGAN原理 | Wasserstein距离、梯度惩罚 |
| 周六 | 2h | StyleGAN | 风格迁移、潜码空间 |
| 周日 | 2h | GAN评估 | FID、IS指标 |

---

### Week 37: 扩散模型

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 扩散模型概述 | 前向过程、反向过程 |
| 周二 | 1h | DDPM原理 | 去噪扩散概率模型 |
| 周三 | 1h | DDPM实现 | PyTorch实现简单DDPM |
| 周四 | 1h | DDIM原理 | 加速采样、确定性生成 |
| 周五 | 1h | 条件生成 | 文本引导图像生成 |
| 周六 | 2h | Stable Diffusion | Diffusers库使用 |
| 周日 | 2h | SD实战 | 文生图、图生图 |

---

### Week 38: 视觉Transformer

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | ViT原理 | Vision Transformer、Patch Embedding |
| 周二 | 1h | ViT实战 | 图像分类 |
| 周三 | 1h | Swin Transformer | 层级结构、窗口注意力 |
| 周四 | 1h | Swin实战 | 目标检测、分割 |
| 周五 | 1h | ConvNeXt | CNN与Transformer融合 |
| 周六 | 2h | DeiT | 数据高效的图像Transformer |
| 周日 | 2h | ViT对比 | ViT vs CNN对比实验 |

---

### Week 39: 3D视觉

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 点云概述 | 点云数据格式、处理 |
| 周二 | 1h | PointNet原理 | 点云分类、分割 |
| 周三 | 1h | PointNet++ | 层次化特征学习 |
| 周四 | 1h | 3D目标检测 | VoxelNet、PointPillars |
| 周五 | 1h | 3D分割 | 点云语义分割 |
| 周六 | 2h | NeRF原理 | 神经辐射场、3D重建 |
| 周日 | 2h | 3D视觉实战 | 简单3D点云项目 |

---

### Week 40: 视频理解

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 视频分类 | 任务定义、数据集 |
| 周二 | 1h | 3D CNN | 时空卷积、C3D、I3D |
| 周三 | 1h | 视频Transformer | ViViT、TimeSformer |
| 周四 | 1h | 动作检测 | 时序动作定位 |
| 周五 | 1h | 视频目标跟踪 | 单目标/多目标跟踪 |
| 周六 | 2h | 视频生成 | 视频预测、扩散模型 |
| 周日 | 2h | 视频理解实战 | 视频分类项目 |

---

### Week 41-42: CV项目实战

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| Week 41 周一 | 1h | 项目选题 | 检测/分割/生成项目选题 |
| Week 41 周二 | 1h | 数据准备 | 数据收集、清洗、增强 |
| Week 41 周三 | 1h | 模型选择 | 选择合适架构 |
| Week 41 周四 | 1h | 基线训练 | 快速建立基线 |
| Week 41 周五 | 1h | 优化调参 | 超参调优 |
| Week 41 周六 | 2h | 错误分析 | 分析失败案例 |
| Week 41 周日 | 2h | 模型改进 | 数据增强、模型集成 |
| Week 42 周一 | 1h | 模型优化 | 继续优化 |
| Week 42 周二 | 1h | 结果分析 | 详细结果分析 |
| Week 42 周三 | 1h | 可视化 | 结果可视化 |
| Week 42 周四 | 1h | 文档撰写 | 项目文档 |
| Week 42 周五 | 1h | 代码整理 | 代码规范化 |
| Week 42 周六 | 2h | 项目总结 | 复盘总结 |
| Week 42 周日 | 2h | 阶段总结 | CV阶段学习总结 |

---

## 📅 阶段五：大模型专题 (第43-52周)

### 📚 学习资源
- Andrej Karpathy《Let's build GPT from scratch》
- Hugging Face LLM课程
- Llama系列论文

---

### Week 43: LLM基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | LLM概述 | 大模型发展历程、规模定律 |
| 周二 | 1h | GPT架构 | GPT-1/2/3架构演进 |
| 周三 | 1h | Llama系列 | Llama 1/2/3架构 |
| 周四 | 1h | 分词器 | BPE、SentencePiece |
| 周五 | 1h | 分词器实战 | 训练自定义分词器 |
| 周六 | 2h | Hugging Face | transformers、datasets库 |
| 周日 | 2h | 模型加载 | 加载和使用预训练LLM |

---

### Week 44: 预训练

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 语言建模 | CLM、MLM、Prefix LM |
| 周二 | 1h | 训练数据 | 数据收集、清洗、去重 |
| 周三 | 1h | 训练技巧 | 混合精度、梯度累积、ZeRO |
| 周四 | 1h | 分布式训练 | 数据并行、模型并行、流水线并行 |
| 周五 | 1h | DeepSpeed | DeepSpeed配置与使用 |
| 周六 | 2h | 预训练实战 | 从头预训练小模型 |
| 周日 | 2h | 训练监控 | Loss曲线、训练稳定性 |

---

### Week 45: 微调技术

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 全参数微调 | 全量参数更新、优缺点 |
| 周二 | 1h | LoRA原理 | 低秩适应、参数高效 |
| 周三 | 1h | LoRA实战 | PEFT库使用LoRA |
| 周四 | 1h | QLoRA | 量化+LoRA、4-bit训练 |
| 周五 | 1h | Adapter | 适配器微调 |
| 周六 | 2h | 其他方法 | Prefix Tuning、P-Tuning |
| 周日 | 2h | 方法对比 | 不同PEFT方法对比实验 |

---

### Week 46: 指令微调

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 指令数据 | 指令数据格式、构造 |
| 周二 | 1h | 指令微调 | SFT训练流程 |
| 周三 | 1h | 数据质量 | 数据筛选、质量评估 |
| 周四 | 1h | Alpaca/Vicuna | 开源指令模型 |
| 周五 | 1h | 指令微调实战 | 微调中文对话模型 |
| 周六 | 2h | 多轮对话 | 多轮对话数据处理 |
| 周日 | 2h | 对话评估 | 人工评估、自动评估 |

---

### Week 47: RLHF基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | RLHF概述 | 强化学习人类反馈 |
| 周二 | 1h | 奖励模型 | 奖励模型训练、Bradley-Terry |
| 周三 | 1h | PPO原理 | Proximal Policy Optimization |
| 周四 | 1h | PPO实战 | trl库实现PPO训练 |
| 周五 | 1h | DPO原理 | Direct Preference Optimization |
| 周六 | 2h | DPO实战 | DPO训练流程 |
| 周日 | 2h | RLHF vs DPO | 对比实验、效果分析 |

---

### Week 48: 对齐技术

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 安全对齐 | 有害内容过滤、安全训练 |
| 周二 | 1h | 偏好数据 | 偏好数据收集、标注 |
| 周三 | 1h | Constitutional AI | Anthropic方法 |
| 周四 | 1h | RLAIF | AI反馈的强化学习 |
| 周五 | 1h | 对齐评估 | 安全性、有用性评估 |
| 周六 | 2h | Red Teaming | 对抗测试、漏洞发现 |
| 周日 | 2h | 对齐实战 | 安全对齐实验 |

---

### Week 49: 推理优化

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | KV Cache | 原理、内存占用 |
| 周二 | 1h | Flash Attention | 内存优化、速度提升 |
| 周三 | 1h | 量化技术 | GPTQ、AWQ、GGML |
| 周四 | 1h | 量化实战 | 模型量化部署 |
| 周五 | 1h | vLLM | 高性能推理框架 |
| 周六 | 2h | 推理优化实战 | 使用vLLM部署 |
| 周日 | 2h | 长文本处理 | RoPE、ALiBi、滑动窗口 |

---

### Week 50: RAG基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | RAG概述 | 检索增强生成原理 |
| 周二 | 1h | 向量数据库 | FAISS、Milvus、ChromaDB |
| 周三 | 1h | 文本嵌入 | Sentence Transformers、BGE |
| 周四 | 1h | RAG流程 | 文档切分、检索、生成 |
| 周五 | 1h | RAG实战 | 简单RAG系统搭建 |
| 周六 | 2h | 检索优化 | 混合检索、重排序 |
| 周日 | 2h | 生成优化 | 提示工程、上下文压缩 |

---

### Week 51: Agent基础

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | Agent概述 | 智能体、工具使用 |
| 周二 | 1h | ReAct框架 | 推理与行动交替 |
| 周三 | 1h | 工具调用 | Function Calling |
| 周四 | 1h | LangChain基础 | 链、代理、工具 |
| 周五 | 1h | LangGraph | 有状态的多步骤Agent |
| 周六 | 2h | Agent实战 | 构建简单Agent |
| 周日 | 2h | Agent评估 | 可靠性、安全性 |

---

### Week 52: 大模型项目实战

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| 周一 | 1h | 项目选题 | 选择LLM应用项目 |
| 周二 | 1h | 数据准备 | 指令数据/检索数据准备 |
| 周三 | 1h | 模型选择 | 选择基础模型 |
| 周四 | 1h | 微调训练 | LoRA/QLoRA微调 |
| 周五 | 1h | RAG集成 | RAG系统搭建 |
| 周六 | 2h | 评估优化 | 效果评估、迭代优化 |
| 周日 | 2h | 项目总结 | 复盘总结、经验提炼 |

---

## 📅 阶段六：前沿方向 (第53-58周)

### Week 53-54: 多模态模型

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| Week 53 周一 | 1h | 多模态概述 | 视觉-语言模型 |
| Week 53 周二 | 1h | CLIP原理 | 对比学习、图文匹配 |
| Week 53 周三 | 1h | CLIP实战 | 零样本图像分类 |
| Week 53 周四 | 1h | BLIP/BLIP-2 | 视觉问答、图像描述 |
| Week 53 周五 | 1h | LLaVA | 多模态大模型 |
| Week 53 周六 | 2h | 多模态实战 | 构建多模态应用 |
| Week 53 周日 | 2h | 视频理解 | 视频-语言模型 |
| Week 54 周一 | 1h | 图像生成 | Stable Diffusion进阶 |
| Week 54 周二 | 1h | ControlNet | 条件控制生成 |
| Week 54 周三 | 1h | IP-Adapter | 图像风格迁移 |
| Week 54 周四 | 1h | 视频生成 | Sora类模型 |
| Week 54 周五 | 1h | 3D生成 | 点云/网格生成 |
| Week 54 周六 | 2h | 多模态综合 | 多模态项目 |
| Week 54 周日 | 2h | 论文阅读 | 多模态前沿论文 |

---

### Week 55-56: AI安全与伦理

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| Week 55 周一 | 1h | AI伦理概述 | 公平性、透明度、可解释性 |
| Week 55 周二 | 1h | 偏见检测 | 模型偏见、数据偏见 |
| Week 55 周三 | 1h | 公平性度量 | 差异影响、机会均等 |
| Week 55 周四 | 1h | 隐私保护 | 差分隐私、联邦学习 |
| Week 55 周五 | 1h | 对抗攻击 | 对抗样本、后门攻击 |
| Week 55 周六 | 2h | 防御技术 | 鲁棒性训练、检测方法 |
| Week 55 周日 | 2h | 可解释性 | SHAP、LIME、注意力可视化 |
| Week 56 周一 | 1h | 安全评估 | Red Teaming、安全基准 |
| Week 56 周二 | 1h | 水印技术 | 文本/图像水印 |
| Week 56 周三 | 1h | 检测生成内容 | AI生成内容检测 |
| Week 56 周四 | 1h | 合规要求 | GDPR、AI法案 |
| Week 56 周五 | 1h | 伦理实践 | 伦理审查流程 |
| Week 56 周六 | 2h | 案例分析 | AI伦理案例研究 |
| Week 56 周日 | 2h | 安全实战 | 构建安全防护系统 |

---

### Week 57-58: 前沿论文与总结

| 日期 | 时长 | 学习内容 | 任务 |
|------|------|----------|------|
| Week 57 周一 | 1h | 论文阅读技巧 | 如何高效阅读论文 |
| Week 57 周二 | 1h | 经典论文精读 | Attention is All You Need |
| Week 57 周三 | 1h | 经典论文精读 | BERT、GPT系列 |
| Week 57 周四 | 1h | 前沿论文 | 2024-2025年最新论文 |
| Week 57 周五 | 1h | 论文复现 | 复现重要论文实验 |
| Week 57 周六 | 2h | 知识体系 | AI算法知识图谱构建 |
| Week 57 周日 | 2h | 面试准备 | 算法面试题整理 |
| Week 58 周一 | 1h | 项目复盘 | 所有项目复盘 |
| Week 58 周二 | 1h | 技术博客 | 整理技术博客 |
| Week 58 周三 | 1h | GitHub整理 | 代码仓库整理 |
| Week 58 周四 | 1h | 简历优化 | 算法工程师简历优化 |
| Week 58 周五 | 1h | 面试模拟 | 模拟面试 |
| Week 58 周六 | 2h | 求职准备 | 技术面准备 |
| Week 58 周日 | 2h | 学习总结 | 完整学习历程总结 |

---

## 📦 数据集资源汇总

### 🎯 通用数据平台

| 平台 | 地址 | 特点 |
|------|------|------|
| **Kaggle** | https://www.kaggle.com/datasets | 最大数据平台，含竞赛数据集 |
| **UCI** | https://archive.ics.uci.edu/ml | 经典机器学习数据集 |
| **Google Dataset Search** | https://datasetsearch.research.google.com | 数据集搜索引擎 |
| **Hugging Face Datasets** | https://huggingface.co/datasets | NLP/多模态数据集 |
| ** Papers With Code** | https://paperswithcode.com/datasets | 论文配套数据集 |
| **天池** | https://tianchi.aliyun.com/datasets | 阿里天池竞赛数据 |
| **data.gov** | https://data.gov | 美国政府开放数据 |

---

### 📊 机器学习阶段数据集 (Week 1-10)

#### 经典入门数据集
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **Titanic** | 二分类 | https://www.kaggle.com/c/titanic | Kaggle入门经典，乘客生存预测 |
| **Iris** | 多分类 | https://archive.ics.uci.edu/ml/datasets/iris | 鸢尾花分类，sklearn内置 |
| **MNIST** | 图像分类 | https://yann.lecun.com/exdb/mnist/ | 手写数字识别，深度学习Hello World |
| **Boston Housing** | 回归 | https://www.kaggle.com/c/boston-housing | 波士顿房价预测(注意伦理问题) |
| **Wine** | 多分类 | https://archive.ics.uci.edu/ml/datasets/wine | 红酒分类，sklearn内置 |
| **Diabetes** | 回归 | sklearn内置 | 糖尿病进展预测 |
| **Breast Cancer** | 二分类 | sklearn内置 | 乳腺癌诊断 |

#### 进阶实战数据集
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **House Prices** | 回归 | https://www.kaggle.com/c/house-prices-advanced-regression-techniques | 房价预测进阶 |
| **Credit Card Fraud** | 异常检测 | https://www.kaggle.com/mlg-ulb/creditcardfraud | 信用卡欺诈检测 |
| **Customer Segmentation** | 聚类 | https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python-for-mall-customers | 客户细分 |
| **Online Retail** | 关联分析 | https://archive.ics.uci.edu/ml/datasets/Online+Retail | 在线零售交易数据 |

---

### 🧠 深度学习阶段数据集 (Week 11-18)

#### 图像分类
| 数据集 | 类别数 | 地址 | 说明 |
|--------|--------|------|------|
| **CIFAR-10** | 10 | https://www.cs.toronto.edu/~kriz/cifar.html | 60k张32x32彩色图像 |
| **CIFAR-100** | 100 | https://www.cs.toronto.edu/~kriz/cifar.html | 60k张32x32彩色图像，100类 |
| **ImageNet** | 1000 | https://image-net.org | 1400万张图像，深度学习标准数据集 |
| **Flowers** | 5 | https://www.tensorflow.org/datasets/catalog/tf_flowers | 3670张花卉图像 |
| **Food-101** | 101 | https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/ | 101种食物分类 |

#### 目标检测
| 数据集 | 类别数 | 地址 | 说明 |
|--------|--------|------|------|
| **PASCAL VOC** | 20 | http://host.robots.ox.ac.uk/pascal/VOC/ | 经典检测数据集 |
| **COCO** | 80 | https://cocodataset.org | 33万图像，大规模检测/分割 |
| **Open Images** | 600 | https://storage.googleapis.com/openimages/web/index.html | 谷歌大规模数据集 |
| **KITTI** | 8 | http://www.cvlibs.net/datasets/kitti/ | 自动驾驶检测数据集 |

#### 图像分割
| 数据集 | 类型 | 地址 | 说明 |
|--------|------|------|------|
| **ADE20K** | 语义分割 | https://groups.csail.mit.edu/vision/datasets/ADE20K/ | 150类，场景理解 |
| **Cityscapes** | 语义分割 | https://www.cityscapes-dataset.com | 城市街景分割 |
| **Lung Segmentation** | 语义分割 | https://www.kaggle.com/andrewmvd/lung-segmentation | 肺部CT分割 |

#### 医学图像
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **ISIC** | 皮肤病变 | https://www.isic-archive.com | 皮肤镜图像 |
| **ChestX-ray14** | 胸部X光 | https://nihcc.app.box.com/v/ChestXray-NIHCC | 胸部疾病诊断 |
| **Ham10000** | 皮肤病变 | https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000 | 10015张皮肤图像 |
| **COVID-CT** | 新冠检测 | https://github.com/UCSD-AI4H/COVID-CT | 新冠CT扫描 |

---

### 📝 NLP阶段数据集 (Week 19-30)

#### 文本分类
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **IMDB** | 情感分析 | https://ai.stanford.edu/~amaas/data/sentiment/ | 50k电影评论，二分类 |
| **SST-2** | 情感分析 | https://huggingface.co/datasets/sst2 | Stanford情感树库 |
| **AG News** | 新闻分类 | https://huggingface.co/datasets/ag_news | 4类新闻分类，12万样本 |
| **Yelp Review** | 情感分析 | https://www.yelp.com/dataset | 评论情感分类 |
| **20 Newsgroups** | 主题分类 | sklearn内置 | 20个新闻组，2万文档 |
| **R8/R52** | 文本分类 | https://www.cs.umb.edu/~leone/r8.html | Reuters新闻分类 |

#### 序列标注
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **CoNLL-2003** | NER | https://huggingface.co/datasets/conll2003 | 命名实体识别经典数据集 |
| **OntoNotes 5.0** | NER/关系 | https://catalog.ldc.upenn.edu/LDC2013T19 | 大规模标注语料 |
| **MSRA-NER** | 中文NER | https://huggingface.co/datasets/msra_ner | 中文命名实体识别 |
| **Resume NER** | 中文NER | https://github.com/jiesutd/RiTA-NER | 中文简历NER |

#### 机器翻译
| 数据集 | 语言对 | 地址 | 说明 |
|--------|--------|------|------|
| **WMT14** | En-De/En-Fr | http://www.statmt.org/wmt14/translation-task.html | 机器翻译标准数据集 |
| **WMT19** | 多语言 | http://www.statmt.org/wmt19/translation-task.html | 最新翻译数据集 |
| **IWSLT** | En-Zh | https://iwslt.org | 口语翻译数据集 |
| **Europarl** | 多语言 | https://www.statmt.org/europarl/ | 欧洲议会语料 |
| **UN Parallel Corpus** | 6语言 | https://conferences.unite.un.org/UNCorpus | 联合国平行语料 |

#### 问答系统
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **SQuAD 2.0** | 阅读理解 | https://rajpurkar.github.io/SQuAD-explorer/ | 斯坦福问答，10万+问题 |
| **Natural Questions** | 阅读理解 | https://ai.google.com/research/NaturalQuestions | Google真实搜索问题 |
| **TriviaQA** | 阅读理解 | https://nlp.cs.washington.edu/triviaqa/ | 问答对数据集 |
| **DuReader** | 中文问答 | https://github.com/baidu/DuReader | 百度中文阅读理解 |

#### 对话系统
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **DailyDialog** | 对话 | http://yanran.li/dailydialog | 日常对话，1万+对话 |
| **PersonaChat** | 对话 | https://huggingface.co/datasets/persona_chat | 个性化对话 |
| **LCCC** | 中文对话 | https://github.com/thu-coai/LCCC | 中文对话数据集 |
| **Douban Conversation** | 中文对话 | https://github.com/Atmae/DoubanConversationCorpus | 豆瓣对话 |

#### 文本生成
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **WikiText-103** | 语言模型 | https://huggingface.co/datasets/wikitext | 维基百科文本 |
| **OpenWebText** | 语言模型 | https://huggingface.co/datasets/openwebtext | 网页文本语料 |
| **Gutenberg** | 语言模型 | https://www.gutenberg.org | 公共领域书籍 |

---

### 🖼️ 计算机视觉阶段数据集 (Week 31-42)

#### 图像分类
| 数据集 | 类别数 | 地址 | 说明 |
|--------|--------|------|------|
| **ImageNet-1K** | 1000 | https://image-net.org | 标准CV benchmark |
| **ImageNet-21K** | 21841 | https://image-net.org | 扩展版ImageNet |
| **Tiny ImageNet** | 200 | https://cs231n.stanford.edu | ImageNet子集，适合学习 |
| **STL-10** | 10 | https://cs.stanford.edu/~acoates/stl10 | 无标签+有标签图像 |

#### 目标检测
| 数据集 | 类别数 | 地址 | 说明 |
|--------|--------|------|------|
| **COCO Detection** | 80 | https://cocodataset.org/#detection | 检测标准数据集 |
| **VisDrone** | 10+ | https://github.com/VisDrone/VisDrone-Dataset | 无人机视角检测 |
| **Open Images V7** | 600 | https://storage.googleapis.com/openimages/web/index.html | 最大规模检测数据集 |
| **LVIS** | 1203 | https://www.lvisdataset.org | 长尾分布检测 |

#### 图像分割
| 数据集 | 类型 | 地址 | 说明 |
|--------|------|------|------|
| **COCO Stuff** | 语义分割 | https://github.com/kyamagu/coco-stuff | COCO扩展分割 |
| **Pascal Context** | 语义分割 | https://host.robots.ox.ac.uk/pascal/VOC/voc2010/ | 59类语义分割 |
| **Matterport3D** | 室内分割 | https://github.com/alexsax/Matterport3D | 3D室内场景 |
| **SBD** | 语义分割 | https://github.com/ShreyasSkand);31/SBD | 扩展VOC分割 |

#### 人脸数据集
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **CelebA** | 人脸属性 | https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html | 20万张人脸，40属性 |
| **LFW** | 人脸识别 | http://vis-www.cs.umass.edu/lfw/ | 人脸验证标准集 |
| **FFHQ** | 人脸生成 | https://nvlabs.github.io/ffhq-dataset/ | 高质量人脸，StyleGAN |
| **VGGFace2** | 人脸识别 | http://www.robots.ox.ac.uk/~vgg/data/face2/ | 9131人脸，330万图像 |

#### 3D视觉数据集
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **ModelNet** | 3D分类 | https://modelnet.stanford.edu | 3D CAD模型 |
| **ShapeNet** | 3D分割 | https://www.shapenet.org | 3D形状数据集 |
| **ScanNet** | 3D分割 | https://www.scan-net.org | 室内3D扫描 |
| **KITTI-3D** | 3D检测 | http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d | 自动驾驶3D检测 |

#### 视频数据集
| 数据集 | 任务 | 地址 | 说明 |
|--------|------|------|------|
| **Kinetics-400** | 动作识别 | https://deepmind.com/research/open-source/kinetics | 400类动作，30万视频 |
| **UCF101** | 动作识别 | https://www.crcv.ucf.edu/data/UCF101.php | 101类动作 |
| **ActivityNet** | 动作检测 | http://activity-net.org | 200类活动检测 |
| **AVA** | 动作检测 | https://research.google.com/ava/ | 时空动作检测 |

---

### 🤖 大模型阶段数据集 (Week 43-52)

#### 预训练语料
| 数据集 | 规模 | 地址 | 说明 |
|--------|------|------|------|
| **The Pile** | 825GB | https://pile.eleuther.ai | 22个子集混合语料 |
| **RedPajama** | 1.2T tokens | https://www.together.ai/blog/redpajama-data-v1 | LLaMA训练数据复现 |
| **RefinedWeb** | 5T tokens | https://huggingface.co/datasets/tiiuae/falcon-refinedweb | 高质量网页语料 |
| **CulturaX** | 6.3T tokens | https://huggingface.co/datasets/uonlp/CulturaX | 多语言清洗语料 |
| **WuDaoCorpora** | 3TB | https://data.baai.ac.cn/details/WuDaoCorpora | 智源中文语料 |
| **SkyPile** | 150B tokens | https://github.com/SkyworkAI/Skywork-13B | 中文网页语料 |

#### 指令微调数据集
| 数据集 | 规模 | 地址 | 说明 |
|--------|------|------|------|
| **Alpaca** | 52k | https://github.com/tatsu-lab/stanford_alpaca | 斯坦福指令数据 |
| **Vicuna** | 125k | https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered | ShareGPT对话数据 |
| **BELLE** | 100k-3.5M | https://github.com/LianjiaTech/BELLE | 中文指令数据 |
| **MOSS** | 1.1B | https://github.com/OpenLMLab/MOSS | 复旦MOSS数据 |
| **Firefly** | 1.1M | https://github.com/Yeachan62/Firefly | 中文多任务指令 |
| **BELLE-2** | 260k | https://github.com/LianjiaTech/BELLE-2 | 中文对话指令 |

#### 偏好数据(RLHF/DPO)
| 数据集 | 规模 | 地址 | 说明 |
|--------|------|------|------|
| **HH-RLHF** | 170k | https://huggingface.co/datasets/Anthropic/hh-rlhf | Anthropic偏好数据 |
| **Stanford SHP** | 385k | https://huggingface.co/datasets/stanfordnlp/Shifting-Layers-and-Preferences | 人类偏好排名 |
| **UltraFeedback** | 64k | https://huggingface.co/datasets/openbmb/UltraFeedback | GPT-4反馈偏好 |
| **Nectar** | 183k | https://huggingface.co/datasets/berkeley-nest/Nectar | 多模型偏好排名 |

#### 中文LLM数据集
| 数据集 | 规模 | 地址 | 说明 |
|--------|------|------|------|
| **C-Eval** | 13k | https://huggingface.co/datasets/ceval/ceval-exam | 中文综合能力评估 |
| **CMMLU** | 11k | https://huggingface.co/datasets/haonan-li/cmmlu | 中文多任务评估 |
| **CMRC** | 16k | https://huggingface.co/datasets/DMetaSoul/squad_chinese | 中文阅读理解 |
| **ChID** | 27k | https://huggingface.co/datasets/chinese-idiom | 中文成语填空 |

---

### 🔗 快速下载命令

#### 使用 Hugging Face Datasets (推荐)
```python
from datasets import load_dataset

# 机器学习
dataset = load_dataset("titanic")

# NLP
dataset = load_dataset("imdb")
dataset = load_dataset("conll2003")
dataset = load_dataset("squad")

# 中文
dataset = load_dataset("clue", "afqmc")
dataset = load_dataset("shibing624/nli_zh", "STS-B")
```

#### 使用 Kaggle CLI
```bash
# 安装
pip install kaggle

# 下载
kaggle competitions download -c titanic
kaggle datasets download -d zalando-research/fashionmnist
```

#### 使用 wget/curl 下载
```bash
# MNIST
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz

# CIFAR-10
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
```

---

### 📋 数据集使用建议

1. **优先使用 Hugging Face Datasets**: 一键加载，自动缓存
2. **Kaggle 竞赛**: 参与比赛是最佳实战方式
3. **小规模试跑**: 先用小数据集调试代码
4. **数据版本管理**: 使用 DVC 或 Git LFS 管理数据
5. **注意数据许可**: 商用需注意License

---

## 📋 每周学习模板

### 工作日 (1小时/天)
```
0-10min:  复习昨日内容
10-50min: 学习新内容(视频/文档)
50-60min: 整理笔记、记录问题
```

### 周末 (2小时/天)
```
0-20min:  复习本周内容
20-90min: 实践练习(代码/项目)
90-120min: 总结反思、规划下周
```

---

## 🎯 学习建议

### 时间管理
- 固定时间段学习(如每天晚上8-9点)
- 利用碎片时间复习笔记
- 周末安排完整项目实践

### 学习方法
- **主动学习**: 不要只看视频，要动手敲代码
- **间隔重复**: 每周回顾之前的内容
- **费曼技巧**: 尝试向别人解释你学到的内容
- **项目驱动**: 每个阶段完成一个实战项目

### 笔记建议
- 使用Obsidian/Notion建立知识库
- 记录重要概念和公式
- 整理代码片段和配置
- 记录踩坑经验和解决方案

### 资源推荐
- **视频**: 李宏毅、吴恩达、Stanford课程
- **书籍**: 西瓜书、统计学习方法、Deep Learning
- **论文**: arXiv、Papers With Code
- **实践**: Kaggle、GitHub开源项目
- **社区**: 知乎、CSDN、机器之心

---

## 📊 学习进度追踪

### 阶段完成度
- [ ] Phase 1: 机器学习基础 (Week 1-10)
- [ ] Phase 2: 深度学习巩固 (Week 11-18)
- [ ] Phase 3: NLP核心 (Week 19-30)
- [ ] Phase 4: 计算机视觉 (Week 31-42)
- [ ] Phase 5: 大模型专题 (Week 43-52)
- [ ] Phase 6: 前沿方向 (Week 53-58)

### 技能树
- [ ] Python编程 ★★★★★
- [ ] NumPy/Pandas ★★★★★
- [ ] 机器学习基础 ★★★★★
- [ ] 深度学习基础 ★★★★★
- [ ] PyTorch框架 ★★★★★
- [ ] NLP技术 ★★★★★
- [ ] 计算机视觉 ★★★★★
- [ ] 大模型技术 ★★★★★
- [ ] 模型部署 ★★★★★
- [ ] 论文阅读 ★★★★★

---

*最后更新: 2026-07-11*
*预计完成时间: 2027年11月*
