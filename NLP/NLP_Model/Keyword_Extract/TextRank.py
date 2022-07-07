# python TextRank.py


import jieba
from jieba import analyse
s = "我出門買早餐順便去打籃球"

print(jieba.analyse.textrank(s,  withWeight=False))
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
