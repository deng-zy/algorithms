# -*- coding: utf-8 -*-
import sys
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

if __name__ == "__main__":
    print sys.argv
    try:
        run_num = sys.argv[1]
    except IndexError:
        run_num = 1

    try:
        list_len = sys.argv[2]
    except IndexError:
        list_len = 12

    ShellSort.main(run_num, list_len)
    sys.exit(0)
