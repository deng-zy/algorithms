# -*- coding: utf-8 -*-
import random
import time


class AbstractSort(object):
    @classmethod
    def sort(cls, origin):
        raise NotImplementedError

    @classmethod
    def generation_list(cls, length, min_num=5, max_num=1000):
        new_list = set([])
        for _ in range(0, length):
            new_list.add(random.randint(min_num, max_num))

        return list(new_list)

    @classmethod
    def main(cls, run_num=None, list_len=None):
        run_num = run_num or random.randint(1, 100)
        list_len = list_len or random.randint(5, 100)
        for i in range(0, run_num):
            source = cls.generation_list(list_len)
            print source
            begin = time.time()
            cls.sort(source)
            print source
            end = time.time()
            print "list numbers:%d, %.4f" % (len(source), end - begin)
