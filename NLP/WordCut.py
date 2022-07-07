
# python WordCut.p


# 1.Preproccess
import jieba.posseg as pseg
import os
import jieba
import numpy as np
import pandas as pd

print(os.getcwd())  # 抓取現在檔案位置
article = pd.read_csv(
    'C:/Users/user/Desktop/Data/AI/AIA/NLP/Excel_data/article_practice.csv')  # 讀取檔案絕對位置路徑
# article.head() # ipynb 才可使用
# type(article['content'])
# article['content']

# filter rules(依據Domain Knowledge去除不需要的資訊  )

# 2.清理資料 :
#   A.將'https?:\/\/\S*' 取代為' '(空值)
article['content'] = article['content'].str.replace('https?:\/\/\S*##', '')

#   B.將 ''(空值) 取代為' '(空)
article['content'] = article['content'].replace('', np.NaN)
# String Split
# ex: 依照文字之間的空格split

article['content'].str.split(" ", n=4, expand=True)
# remove data

# remove NaN
article = article.dropna()

# 讓index重置成原本的樣子
article = article.reset_index(drop=True)

article['idx'] = article.index
print(article['idx'])

# 3.Jieba(Word Cut Tool)
# set dictionary (can define yourself)
os.getcwd()
jieba.set_dictionary(
    'C:/Users/user/Desktop/Data/AI/AIA/NLP/jieba/dict.txt.big')
stop_words = open('C:/Users/user/Desktop/Data/AI/AIA/NLP/jieba/stop_words.txt',
                  encoding="utf-8").read().splitlines()
print(stop_words[:300])

# Data type "Pandas Dataframe" to "list"

data = pd.read_csv(
    'C:/Users/user/Desktop/Data/AI/AIA/NLP/Excel_data/article_preprocessed.csv')
data = data['content'].tolist()
print(data[:20])

# 4.詞性處理(Posseg) :
for w, f in pseg.cut(data[0]):
    print(w, ' ', f)
