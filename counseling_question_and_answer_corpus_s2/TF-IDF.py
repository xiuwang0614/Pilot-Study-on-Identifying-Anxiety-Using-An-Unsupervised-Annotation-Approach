# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:06:55 2022

@author: dell
"""


# encoding=utf-8
import uniout  # 编码格式，解决中文输出乱码问题
import csv
import re
import pandas as pd
import jieba
from os import path  #用来获取文档的路径
import jieba.analyse as ana
import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

if __name__ == '__main__':
    
     with open(r"C:\Users\dell\Desktop\毕设\数据分析\语料库数据分析\step1\resultt.csv", 'r') as f:

        text_read = f.read()  #读取文件

    
     word_list=ana.extract_tags(text_read,topK=500,withWeight=True) #去除停用词+词频分析
     word_dict = {} #转化为字典形式以便做词云图
     for i in word_list:
         word_dict[i[0]]=i[1]
        
     print(word_dict)
    

