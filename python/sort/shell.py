# -*- coding: utf-8 -*-
from sort import AbstractSort


class ShellSort(AbstractSort):
    @classmethod
    def sort(cls, origin):
        length = len(origin)
        segment = 1
        while segment < length / 3:
            segment = 3 * segment + 1

        while segment >= 1:
            for i in range(segment, length):
                # print "{}-{}".format(segment, i)
                j = i
                while j >= segment:
                    # print "{}-{}".format(i, j)
                    if origin[j] < origin[j - segment]:
                        tmp = origin[j]
                        origin[j] = origin[j - segment]
                        origin[j - segment] = tmp
                    j -= segment

            segment = segment / 3
