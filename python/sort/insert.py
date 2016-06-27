# -*- coding: utf-8 -*-
import sys
from sort import AbstractSort


class InsertSort(AbstractSort):
    @classmethod
    def sort(cls, origin):
        length = len(origin)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if origin[j] < origin[j - 1]:
                    tmp = origin[j]
                    origin[j] = origin[j - 1]
                    origin[j - 1] = tmp

if __name__ == "__main__":
    InsertSort.main()
    sys.exit(0)
