# -*- coding: utf-8 -*-
import sys
from sort import AbstractSort


class SelectionSort(AbstractSort):
    @classmethod
    def sort(cls, origin):
        length = len(origin)
        for i in range(0, length):
            min_index = i
            for j in range(i+1, length):
                if origin[j] < origin[min_index]:
                    min_index = j

            tmp = origin[i]
            origin[i] = origin[min_index]
            origin[min_index] = tmp


if __name__ == "__main__":
    SelectionSort.main()
    sys.exit(0)
