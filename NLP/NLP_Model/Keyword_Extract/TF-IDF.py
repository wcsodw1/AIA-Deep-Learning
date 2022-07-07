# python TF-IDF.py
# Descibe: TF-IDF為抓取文字當中關鍵字的一種方法(工具)
"""
TF (Term Frequency)「詞頻」指的是一個詞在一個文件中出現的頻率，因此一個詞TF越高，可能就代表他在這篇文章中沒那麼重要
例如英文的 “the”, “a” 還有中文的「的」、「了」等等，這些字都很常出現，但沒什麼意義。
"""

import jieba
import jieba.analyse


# Example1 :
text = '總統蔡英文論文風波延燒後，最新民調今日出爐！據親藍民調公布結果，蔡英文支持度45%，遙遙領先韓國瑜的33%，兩人差距擴大到12個百分點。顯示論文門風波，並未重創小英聲望。'
tags = jieba.analyse.extract_tags(text, topK=5)
# topK 為返回幾個TF/IDF 權重最大的關鍵詞，默認值為20
print(tags)
print("================")


# Example2 :
s = "我出門買早餐, 順便去打籃球"
print("=== Example2 ===")
print(jieba.analyse.extract_tags(s, topK=20, withWeight=False, allowPOS=()))
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))
