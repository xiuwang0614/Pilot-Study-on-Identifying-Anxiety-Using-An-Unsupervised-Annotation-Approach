# -*- coding: utf-8 -*-

import uniout  # 编码格式，解决中文输出乱码问题
import csv
import re
import pandas as pd
import jieba
from os import path  #用来获取文档的路径
import jieba.analyse as anls
from PIL import Image
import numpy as  np
import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm

#背景图
bg=np.array(Image.open("background.jpg"))

#获取当前的项目文件加的路径
d=path.dirname(__file__)

# 读取文本
df = pd.read_csv(r"C:\Users\dell\Desktop\毕设\数据分析\问卷\daima\source.csv",engine = 'python').astype(str)

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
inputs=df["内容"]

line_seg=[]

for line in inputs:
   line_seg.append(seg_sentence(line))  
name = ['内容']
test = pd.DataFrame(columns=name,data=line_seg)
print(test) 
test.to_csv(r"C:\Users\dell\Desktop\毕设\数据分析\问卷\daima\result3.csv",encoding='ANSI')

fW = open('result.csv','w',encoding = 'gbk')
fW.write(' '.join(line_seg))
fW.close()
line_seg_str =' '.join(line_seg)#list类型分为str

with open('result.csv',"r",encoding = 'gbk') as r:
                lines =r.readlines()
with open('result.csv',"w",encoding = 'gbk') as w:
                for line in lines:
                       if len(line) > 2:
                           w.write(line)

fW = open('result.csv','w',encoding = 'gbk')
fW.write(' '.join(line_seg))
fW.close()

text_split_no_str =' '.join(line_seg)  #list类型分为str

#基于tf-idf提取关键词
print("基于TF-IDF提取关键词结果：")
keywords = []
for x, w in anls.extract_tags(text_split_no_str, topK=200, withWeight=True):
    keywords.append(x)   #前200关键词组成的list
keywords = '\n'.join(keywords)   #转为str

print(keywords)
print("基于词频统计结果")

txt = open("result.csv", "r", encoding="gbk").read()
words = jieba.cut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(33):
    word, count=items[i]
    print((word),count)



wc=WordCloud(
    background_color="white",
    max_words=200,
    mask=bg,            #设置词云形状,改为mask =None;默认生成矩形图云
    max_font_size=60,
    scale=16,
    random_state=42,
    mode='RGBA', 
    width=800,
    height=600,
    font_path='simhei.ttf'   #中文处理，用国标黑体字体，如果系统没有需将附件的字体文件放到代码目录下
    ).generate(keywords)
#为图片设置字体
my_font=fm.FontProperties(fname='simhei.ttf.ttf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(bg)
#开始画图

plt.imshow(wc)
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
#plt.figure()
plt.show()
#为背景图去掉坐标轴
plt.axis("off")
plt.imshow(bg,cmap=plt.cm.gray)
#plt.show()

#保存云图
wc.to_file("ciyun.png")
print("词云图片已保存")
