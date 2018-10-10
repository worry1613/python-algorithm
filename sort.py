# -*- coding: utf-8 -*-
# @创建时间 : 9/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
import copy
import random


def insertsort(s):
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
            print('====', s)
            j -= 1
            c += 1
        s[j] = x
    print(c)


def selectsort(s):
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
                print('i=',i,'j=',j,'min=',min)
                c += 1
        if i != min:
            s[i], s[min] = s[min], s[i]
    print(c)

def bubblesort(s):
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
        for j in range(1,len(s)-i):
            if s[j-1] > s[j]:
                print('j-1=', j - 1, 'j=', j)
                s[j-1], s[j] = s[j], s[j-1]
                print(s)
                c += 1
        print(s)
    print(c)


def quicksort(s, start, end):
    """
    快速排序
    :param end: 结束下标
    :param start: 起始下标
    :param s:   要排序的数组
    :return :


    """
    print('<<<<',s,'start=',start,'end=',end)
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
        print('%4d %s low=%d high=%d ' % (c, s, low, high))
        while low < high and s[low] <= key:
            low += 1
        s[high] = s[low]
        print('%4d %s low=%d high=%d ' % (c, s, low, high))
    s[low] = key

    print('%4d %s low=%d high=%d ' % (c,s,low,high))
    print('>>>>',s)
    quicksort(s, start, low-1)
    quicksort(s,low+1,end)
    print('>>>>', s)

def quicksort2(s, start, end):
    """
    快速排序
    :param end: 结束下标
    :param start: 起始下标
    :param s:   要排序的数组
    :return :


    """

    if start >= end:
        return
    print('<<<<', s, 'start=', start, 'end=', end)
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
            print('1      high=',high,'s[high]=',s[high],'low=',low,'s[low]=',s[low])
            s[high], s[low] = s[low], s[high]
            print('2      high=',high,'s[high]=',s[high],'low=',low,'s[low]=',s[low])
        print('%4d %s low=%d high=%d ' % (c, s, low, high))
    print('3      start=', start, 'low=', low, 's[low]=', s[low])
    s[start],s[low] = s[low],s[start]
    print('4      start=', start, 'low=', low, 's[low]=', s[low])
    print('%4d %s low=%d high=%d ' % (c,s,low,high))

    quicksort2(s, start, low-1)
    quicksort2(s,low+1,end)



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

    intsrand = [random.randint(0,100) for i in range(20)]
    intsrand2 = copy.copy(intsrand)
    # print(intsrand)
    quicksort(intsrand,0,len(intsrand)-1)
    for i in range(20):
        print('//////////////////////')

    quicksort2(intsrand2,0,len(intsrand2)-1)
    # print(intsrand)
