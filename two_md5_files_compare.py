#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import difflib
import time

fileA='/path/to/file1'
fileB='/path/to/file2'

def time_cont(filediff):
    def time1(a,b):
        start = time.time()
        filediff(a,b)
        end = time.time()
        print(end - start)
    return time1
# 装饰器
@time_cont
def filediff(fileA,fileB):
    return set(open(fileB,encoding='gb18030').readlines())-set(open(fileA,encoding='gb18030').readlines())

print(filediff(fileA,fileB))

