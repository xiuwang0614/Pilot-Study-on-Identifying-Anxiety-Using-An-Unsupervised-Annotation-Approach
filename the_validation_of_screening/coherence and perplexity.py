# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:05:04 2022

@author: dell
"""

from gensim import corpora, models
import math
import pyLDAvis.gensim
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import pandas as pd
import re
import jieba
from pprint import pprint

import os
import sys
sys.stderr = open(os.devnull, "w")  # silence stderr
import gensim
import mallet
#from gensim import wrappers
import gensim.corpora as corpora
from gensim.models import CoherenceModel
sys.stderr = sys.__stderr__  # unsilence stderr

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # 3.3.x 版本之前请使用 import pyLDAvis.gensim
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

if __name__ == '__main__':
    cop = open(r"C:\Users\dell\Desktop\毕设\数据分析\validity\2-step1.csv")
    train = []
    for line in cop.readlines():
        line = [word.strip() for word in line.split(' ')]
        train.append(line)
    #print(train)
    
    id2word = corpora.Dictionary(train)
    corpus = [ id2word.doc2bow(sentence) for sentence in train]
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    #print(id2word)
    #print(corpus)

    '''模型复杂度和主题一致性提供了一种方便的方法来判断给定主题模型的好坏程度。特别是主题一致性得分更有帮助。'''
    model_list = []
    perplexity = []
    coherence_values = []
    for num_topics in range(1,50,1):
        lda_model = models.LdaModel(corpus=corpus_tfidf,
                                    id2word=id2word,
                                    random_state=1,
                                    num_topics=num_topics,# random_state=100,# update_every=1,# chunksize=100,# passes=10,# alpha='auto',# per_word_topics=True
                                    )    
        model_list.append(lda_model)#计算困惑度    
        perplexity_values = lda_model.log_perplexity(corpus)    
        print('%d 个主题的Perplexity为: ' % (num_topics+1), perplexity_values) # a measure of how good the model is. lower the better.    
        perplexity.append(perplexity_values)
    #计算一致性    
        coherencemodel = CoherenceModel(model=lda_model, texts=train, dictionary=id2word, coherence='c_v')    
        coherence_values.append(round(coherencemodel.get_coherence(),3))    
        print('%d 个主题的Coherence为: ' % (num_topics+1), round(coherencemodel.get_coherence(),3))

                                                                      
#用subplot()方法绘制多幅图形
    plt.figure(figsize=(16,5),dpi=200)
    x = range(1,50,1)#将画板划分为2行1列组成的区块，并获取到第一块区域
    ax1 = plt.subplot(1,2,1)#在第一个子区域中绘图
    plt.plot(x,perplexity)
    plt.xlabel("Num Topics")
    plt.ylabel("Perplexity score")
    plt.xticks(range(1,50,2))
    #设置刻度plt.title('困惑度')
    plt.grid(True, alpha=0.5)
    #选中第二个子区域，并绘图
    ax2 = plt.subplot(1,2,2)
    plt.plot(x,coherence_values)
    plt.xlabel("Num Topics")
    plt.ylabel("Coherence score")
    plt.xticks(range(1,50,1))
#设置刻度plt.title('一致性')
    plt.grid(True, alpha=0.5)
    plt.savefig('./困惑度与一致性.png', dpi=300)                                                                