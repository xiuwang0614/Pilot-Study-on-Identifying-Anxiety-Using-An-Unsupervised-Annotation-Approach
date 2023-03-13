# -*- coding: utf-8 -*-

import uniout  # 编码格式，解决中文输出乱码问题
import pandas as pd
import re
import csv
import jieba

# 读取文本
df = pd.read_csv(r"C:\Users\dell\Desktop\毕设\数据分析\weibo\weiboo.csv",engine = 'python').astype(str)

# 读取停用词表
def stopwordslist():
    stopwords = [line.strip() for line in open(r"C:\Users\dell\Desktop\毕设\数据分析\语料库数据分析\step1\stopwords.txt",encoding='utf-8'
).readlines()] 
    return stopwords

# 自定义词典
jieba.load_userdict(r"C:\Users\dell\Desktop\毕设\数据分析\语料库数据分析\step1\userdict.txt")

def seg_sentence(sentence):


    # 每一行分词
    sentence_seged = jieba.cut(sentence.strip())

    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_seged:
        # 不在停用词表里并且长度大于1
        # 并将分分词结果用空格连接
        if word not in stopwords and len(word) > 1 :
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
inputs=df['微博正文']

line_seg=[]

for line in inputs:
   line_seg.append(seg_sentence(line))  
name = ['微博正文']
test = pd.DataFrame(columns=name,data=line_seg)
print(test) 
test.to_csv(r"C:\Users\dell\Desktop\毕设\数据分析\weibo\result.csv",encoding='ANSI')

