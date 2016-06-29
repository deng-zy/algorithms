# -*- coding: utf-8 -*-
from . import AbstractSort


class QuickSort(AbstractSort):

    @classmethod
    def sort(cls, origin):
        cls._sort(origin, 0, len(origin) - 1)

    @classmethod
    def _sort(cls, origin, left, right):
        if left > right:
            return

        base = origin[left]
        i = left
        j = right

        while i != j:
            while origin[j] >= base and i < j:
                j -= 1

            while origin[i] <= base and i < j:
                i += 1

            if i < j:
                tmp = origin[i]
                origin[i] = origin[j]
                origin[j] = tmp

        origin[left] = origin[j]
        origin[i] = base

        cls._sort(origin, left, i - 1)
        cls._sort(origin, i + 1, right)
