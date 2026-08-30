import jieba
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from config import RAW_DATA_PATH
import config 


def build_data_set(sentences,word2index):
    indexed_sentences = [[word2index.get(token,0) for token in jieba.lcut(sentence)] for sentence in sentences]

    dataset = []

    for sentence in indexed_sentences:
        for i in range(len(sentence)-config.SEQ_LEN):
            input = sentence[i:i+config.SEQ_LEN]
            target = sentence[i+config.SEQ_LEN]
            dataset.append({'input':input,'target':target})
    return dataset

def process():
    print('开始处理数据')
    # 1. 读取文件
    df = pd.read_json(RAW_DATA_PATH/'synthesized_.jsonl',orient='records',lines=True)
    # print(df.head())
    # 2. 提取句子
    sentences = []
    for dialog in df['dialog']:
        for sentence in dialog:
            sentences.append(sentence.split("：")[1])

    # print(sentences[0:10])
    # print('句子总数：',len(sentences))

    # 3. 划分数据集
    train_sentences,test_sentences = train_test_split(sentences,test_size=0.2)

    # 4. 构建词表
    vocab_set = set()
    for sentence in tqdm(train_sentences,desc="构建词表"):
        vocab_set.update(jieba.lcut(sentence))
        
    
    vocat_list = ['<unk>'] + list(vocab_set)
    
    # 5. 保存词表
    with open(config.MODELS_DIR/'vocab.txt','w',encoding='utf-8') as f:
        f.writelines(f"{word}\n" for word in vocat_list)

    # 6. 构建训练集
    word2index = {word: index for index,word in enumerate(vocat_list)}
    train_dataset = build_data_set(train_sentences,word2index)
    # print(train_dataset[0:3])
    # 7. 保存训练集
    pd.DataFrame(train_dataset).to_json(config.PROCESSED_DIR_PATH/'train.jsonl',orient='records',lines=True)

    # 8. 构建测试集
    test_dataset = build_data_set(test_sentences,word2index)
    # 9. 保存测试集
    pd.DataFrame(test_dataset).to_json(config.PROCESSED_DIR_PATH/'test.jsonl',orient='records',lines=True)

    print('数据处理完成')





if __name__ == '__main__':
    process()