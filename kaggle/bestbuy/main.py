# -*- coding: utf-8 -*-

import pandas as pd;
from sklearn.model_selection import train_test_split
import Levenshtein
import operator

# __train__ = './data/train_sample.csv'
__train__ = './data/train.csv'
__test__ = './data/test.csv'

def load_data():
    data = pd.read_csv(__train__, sep=',')
    X = data['query'].values.reshape(-1, 1)
    X = preprocess(X, 0)
    y = data['sku'].values.reshape(-1, 1)
    return data, X, y

# 只需要是数字和字母的
def string_process(str):
    res = str.replace(' ','')
    res = res.lower()
    res = ''.join(c for c in res if c.isalnum())
    return res

def preprocess(data, column):
    for row in data:
        row[column] = string_process(row[column])
    return data

def evaluate(predict, label):
    total = 0.0
    right = 0.0
    for pre, lab in zip(predict, label):
        total += 1
        if lab[0] in pre:
            right += 1
    return right / total

class Model:
    '''
    query1
        + sku1 => cout
        + sku3 => cout2
    query2
        ...
    '''
    __query_sku = {}
    __sku_cout = {}
    merge_threshold = 0
    predict_threshold = 0
    def __init__(self, merge_threshold=0.5, predict_threshold=0.5):
        self.merge_threshold = merge_threshold
        self.predict_threshold = predict_threshold

    def __match_query(self, querys, cur_query):
        max_sim = 0
        best_match_query = None
        for query in querys:
            sim = Levenshtein.ratio(query, cur_query)
            if sim > max_sim:
                max_sim, best_match_query = sim, query
        return best_match_query, max_sim

    def fit(self, X_train, y_train):
        # 获得排名最高的商品 用于补足
        # self.__sku_cout
        self.__get_top(X_train, y_train)

        # 获取每个query下和商品点击数之间的关系
        # self.__query_sku
        self.__fit(X_train, y_train)

    def __fit(self, X_train, y_train):
        for x, y in zip(X_train, y_train):
            x = x[0]
            y = y[0]
            match_query = None
            best_match_query, max_sim = self.__match_query(self.__query_sku.keys(), x)
            if max_sim > self.merge_threshold:
                match_query = best_match_query
            else:
                self.__query_sku[x] = {y : 1}

            if match_query is None:
                continue
            if not self.__query_sku[match_query].has_key(y):
                self.__query_sku[match_query][y] = 1
            else:
                self.__query_sku[match_query][y] += 1

        # 按照sku次数排序
        for query in self.__query_sku.keys():
            tmp = self.__query_sku[query]
            tmp = sorted(tmp.iteritems(), key=operator.itemgetter(1), reverse=True)
            self.__query_sku[query] = tmp

    def __get_top(self, X_train, y_train):
        for x, y in zip(X_train, y_train):
            x = x[0]; y = y[0]
            if not self.__sku_cout.has_key(y):
                self.__sku_cout[y] = 1
            else:
                self.__sku_cout[y] += 1
        self.__sku_cout = sorted(self.__sku_cout.items(), key=lambda d:d[1], reverse=True)

    def predict(self, X_test, predict_num):
        res = []
        for query in X_test:
            predict_sku = []
            query = query[0]
            best_match_query, max_sim = self.__match_query(self.__query_sku.keys(), query)
            if max_sim > self.predict_threshold:
                for query_sku in self.__query_sku[best_match_query][0:predict_num]:
                    predict_sku += [query_sku[0]]

            # 匹配不足就用最常用的补充
            if (len(predict_sku) < predict_num):
                for top_sku in self.__sku_cout:
                    if top_sku[0] not in predict_sku:
                        predict_sku += [top_sku[0]]
                    if len(predict_sku) == predict_num:
                        break
            # print predict_sku
            res.append(predict_sku)
        return res


if __name__ == "__main__":
    data, X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    model = Model(merge_threshold=0.85, predict_threshold=0.5)
    model.fit(X_train, y_train)
    predict = model.predict(X_test, predict_num = 5)
    accuracy = evaluate(predict, y_test)
    print accuracy

