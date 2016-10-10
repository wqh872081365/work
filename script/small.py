# -*- coding: utf-8 -*-

# 全排列
# wangqihui
# 2016-10-10

import itertools

list1 = 'ABCDEF'
list2 = []

for i in range(1, len(list1)+1):
    iter1 = itertools.combinations(list1, i)

    list2 += (list(iter1))

# print list2
for l1 in list2:
    print ''.join(l1)

#
