# -*- coding: utf-8 -*-
# @创建时间 : 9/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
import copy
import random


def insertsort(s, debug=1):
    """
    插入排序
    :param s:   要排序的数组
    :return s:  排序后的数组

    for i in range(len(s)):
        将大于s[i]的所有元素s[j]都移动一个位置，将s[i]放到合适的位置上
    """
    c = 0
    for i in range(len(s)):
        x = s[i]
        j = i
        while j > 0 and s[j - 1] > x:
            s[j] = s[j - 1]
            print('====', s) if debug else None
            j -= 1
            c += 1
        s[j] = x
    print(c) if debug else None


def shellsort(s, debug=1):
    """
    希尔排序
    :param s:   要排序的数组
    :return s:  排序后的数组


    """
    c = 0
    n = len(s)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if s[i] < s[i - gap]:
                    s[i], s[i - gap] = s[i - gap], s[i]
                    i -= gap
                    print('====', s, 'i=', i, 'gap=', gap) if debug else None
                    c += 1
                else:
                    break

        gap //= 2
        print('=+=+', s) if debug else None
    print(c)


def shellsort2(s, debug=1):
    """
    希尔排序
    :param s:   要排序的数组
    :return s:  排序后的数组

    c++数据结构与算法 第四版中提出的
    gap=3*gap+1
    """
    c = 0
    n = len(s)
    gap = 1
    gaps = []
    while gap < n:
        gaps.insert(0, gap)
        gap = 3 * gap + 1
    for g in range(len(gaps)):
        gap = gaps[g]
        for j in range(gap, n):
            i = j
            while i > 0:
                if s[i] < s[i - gap]:
                    s[i], s[i - gap] = s[i - gap], s[i]
                    i -= gap
                    print('|===', s, 'i=', i, 'gap=', gap) if debug else None
                    c += 1
                else:
                    break
        print('=+=+', s) if debug else None
    print(c)


def selectsort(s, debug=1):
    """
    选择排序
    :param s:   要排序的数组
    :return :

    for i in range(len(s)-1)
        找出元素s[i]….s[len(s)]中的最小元素
        与s[i]交换

    """
    c = 0
    for i in range(len(s) - 1):
        min = i
        for j in range(i, len(s)):
            if s[j] < s[min]:
                min = j
                print('i=', i, 'j=', j, 'min=', min) if debug else None
                c += 1
        if i != min:
            s[i], s[min] = s[min], s[i]
    print(c)


def mergesort(s, debug=1):
    """
    归并排序
    :param s:   要排序的数组
    :return :

    for i in range(len(s)-1)
        找出元素s[i]….s[len(s)]中的最小元素
        与s[i]交换

    """

    def sort(a):
        n = len(a)
        if n <= 1:
            return a
        mid = n // 2
        print('<<<<mid=', mid) if debug else None
        left = sort(a[:mid])
        print('>>>>mid=', mid) if debug else None
        right = sort(a[mid:])
        return merge(left, right)

    def merge(l, r):
        left, right = 0, 0
        nl = len(l)
        nr = len(r)
        result = []
        while left < nl and right < nr:
            if l[left] <= r[right]:
                result.append(l[left])
                left += 1
            else:
                result.append(r[right])
                right += 1
            print(l, r) if debug else None
        result += l[left:]
        result += r[right:]
        print(l, r, result) if debug else None
        return result
    print('++++', s) if debug else None
    return sort(s)


def bubblesort(s, debug=1):
    """
    冒泡排序
    :param s:   要排序的数组
    :return :

    for i in range(len(s)-1)
        找出元素s[i]….s[len(s)]中的最小元素
        与s[i]交换

    """
    c = 0
    for i in range(len(s) - 1):
        for j in range(1, len(s) - i):
            if s[j - 1] > s[j]:
                print('j-1=', j - 1, 'j=', j) if debug else None
                s[j - 1], s[j] = s[j], s[j - 1]
                print(s) if debug else None
                c += 1
        print(s) if debug else None
    print(c)


def quicksort(s, start, end, debug=1):
    """
    快速排序
    :param end: 结束下标
    :param start: 起始下标
    :param s:   要排序的数组
    :return :


    """
    print('<<<<', s, 'start=', start, 'end=', end) if debug else None
    if start >= end:
        return
    c = 0
    low = start
    high = end
    key = s[start]
    while low != high:
        while low < high and s[high] >= key:
            high -= 1
        s[low] = s[high]
        print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None
        while low < high and s[low] <= key:
            low += 1
        s[high] = s[low]
        print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None
    s[low] = key

    print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None
    print('>>>>', s) if debug else None
    quicksort(s, start, low - 1)
    quicksort(s, low + 1, end)
    print('>>>>', s) if debug else None


def quicksort2(s, start, end, debug=1):
    """
    快速排序
    :param end: 结束下标
    :param start: 起始下标
    :param s:   要排序的数组
    :return :


    """

    if start >= end:
        return
    print('<<<<', s, 'start=', start, 'end=', end) if debug else None
    c = 0
    low = start
    high = end
    key = s[start]
    while low != high:
        while low < high and s[high] >= key:
            high -= 1
        while low < high and s[low] <= key:
            low += 1
        if low < high:
            print('1      high=', high, 's[high]=', s[high], 'low=', low, 's[low]=', s[low]) if debug else None
            s[high], s[low] = s[low], s[high]
            print('2      high=', high, 's[high]=', s[high], 'low=', low, 's[low]=', s[low]) if debug else None
        print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None
    print('3      start=', start, 'low=', low, 's[low]=', s[low]) if debug else None
    s[start], s[low] = s[low], s[start]
    print('4      start=', start, 'low=', low, 's[low]=', s[low]) if debug else None
    print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None

    quicksort2(s, start, low - 1)
    quicksort2(s, low + 1, end)


def quicksort3(s, start, end, debug=1):
    """
    快速排序
    :param end: 结束下标
    :param start: 起始下标
    :param s:   要排序的数组
    :return :


    """

    if start >= end:
        return
    print('<<<<', s, 'start=', start, 'end=', end) if debug else None
    c = 0
    low = start
    high = end
    key = s[start]
    for j in range(start + 1, end + 1):
        if s[j] < key:
            low += 1
            s[j], s[low] = s[low], s[j]
            if debug:
                print('+-+-', s)
    print('3      start=', start, 'low=', low, 's[low]=', s[low]) if debug else None
    s[start], s[low] = s[low], s[start]
    print('4      start=', start, 'low=', low, 's[low]=', s[low]) if debug else None
    print('%4d %s low=%d high=%d ' % (c, s, low, high)) if debug else None

    quicksort3(s, start, low - 1)
    quicksort3(s, low + 1, end)


def test_sortinsert(s):
    print('################sortinsert#####################')
    print('++++', s)
    insertsort(s)
    print('++++', s)


def test_sortselect(s):
    print('################sortselect#####################')
    print('++++', s)
    selectsort(s)
    print('++++', s)


def test_sortbubble(s):
    print('################sortbubble#####################')
    print('++++', s)
    bubblesort(s)
    print('++++', s)


if __name__ == '__main__':
    ints1 = [i for i in range(20)]
    ints2 = ints1[::-1]
    test_sortinsert(ints1)
    test_sortinsert(ints2)

    ints1 = [i for i in range(20)]
    ints2 = ints1[::-1]
    test_sortselect(ints1)
    test_sortselect(ints2)

    ints1 = [i for i in range(20)]
    ints2 = ints1[::-1]
    test_sortbubble(ints1)
    test_sortbubble(ints2)

    intsrand = [random.randint(0, 1000) for i in range(10)]
    intsrand2 = copy.copy(intsrand)
    intsrand3 = copy.copy(intsrand)
    intsrand4 = copy.copy(intsrand)
    intsrand5 = copy.copy(intsrand)
    intsrand6 = copy.copy(intsrand)
    # print(intsrand)
    quicksort(intsrand, 0, len(intsrand) - 1)
    for i in range(5):
        print('//////////////////////')
    quicksort2(intsrand2, 0, len(intsrand2) - 1)
    for i in range(5):
        print('//////////////////////')
    quicksort3(intsrand3, 0, len(intsrand3) - 1)
    # print(intsrand)
    for i in range(5):
        print('//////////////////////')
    newstr = mergesort(intsrand4)
    print(newstr)
    intsrand.sort()

    for i in range(5):
        print('//////////////////////')
    shellsort(intsrand5)
    print(intsrand5)
    for i in range(5):
        print('//////////////////////')
    shellsort2(intsrand6,debug=0)
    print(intsrand6)
