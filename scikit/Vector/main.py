# -*- coding: utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
v = DictVectorizer(sparse=False)
D = [{'foo': 'd', 'bar': 2.3}, {'foo': 'f', 'baz': 1.5}]
X = v.fit_transform(D)
print v.feature_names_