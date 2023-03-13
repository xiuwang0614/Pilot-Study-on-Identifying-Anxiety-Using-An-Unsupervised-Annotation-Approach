# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:01:31 2022

@author: dell
"""

def average_top_3(matric):
    result = []
    for vec in matric:
        index_1, index_2, index_3 = None, None, None
        max = 0

        for n,i in enumerate(vec):
            if i > max:
                max = i
                index_1 = n
        top_1 = max
        max = 0

        for n,i in enumerate(vec):
            if (i != top_1 or n != index_1) and  i > max:
                max = i
                index_2 = n
        top_2 = max
        max = 0

        for n,i in enumerate(vec):
            if  (n != index_1) and (n != index_2)  and i > max:
                max = i
        top_3 = max
        result.append((top_1 + top_2 + top_3)/3)
    return result

raw_dict = [line.strip() for line in open(r"C:\Users\dell\Desktop\毕设\数据分析\weibo\dic.csv").readlines()]

weibo_text = [line.strip() for line in open(r"C:\Users\dell\Desktop\毕设\数据分析\weibo\PPT.csv").readlines()]

from gensim.models import KeyedVectors

lib_path = r"C:\Users\dell\Desktop\毕设\tencent-ailab-embedding-zh-d200-v0.2.0-s\tencent-ailab-embedding-zh-d200-v0.2.0-s.txt"
wv_from_text = KeyedVectors.load_word2vec_format(lib_path, binary=False)

result = []
for line in weibo_text:
    mat = []
    for word in line.split(' '):
        line = []
        for corpus in raw_dict:
            if corpus == word:
                line.append(1)
            else:
                try:
                    similarity = wv_from_text.similarity(corpus, word)
                    line.append(similarity)
                except Exception as e:
                    #print("未知错误：",e)
                
                    #print(corpus, " and ",word)
                    line.append(0)
        mat.append(max(line))
        line = []
    print(mat)
    result.append(mat)
    mat = []
print(result)
f = open('matric.txt', 'w')
f.write(str(result))
f.close()

f = open('result.txt', 'w')
f.write(str(average_top_3(result)))
f.close()