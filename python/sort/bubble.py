# -*- coding: utf-8 -*-
from sort import AbstractSort


class BubbleSort(AbstractSort):

    @classmethod
    def sort(cls, origin):
        length = len(origin)
        for i in range(0, length):
            j = 0
            while j < length - 1:
                if origin[j] > origin[j + 1]:
                        tmp = origin[j + 1]
                        origin[j + 1] = origin[j]
                        origin[j] = tmp
                j += 1

