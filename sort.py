# -*- coding: utf-8 -*-
# @创建时间 : 9/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/


def sortinsert(s):
    """
    插入排序
    :param s:   要排序的数组
    :return s:  排序后的数组
    """
    c=0
    for i in range(len(s)):
        x = s[i]
        j = i
        while j>0 and s[j-1] > x:
            s[j] = s[j-1]
            print('====',s)
            j-=1
            c+=1
        s[j]=x
    print(c)

def sortselect(s):
    """
    选择排序
    :param s:   要排序的数组
    :return :
    """
    c=0
    for i in range(len(s)):
        x = s[i]
        j = i
        while j>0 and s[j-1] > x:
            s[j] = s[j-1]
            print('====',s)
            j-=1
            c+=1
        s[j]=x
    print(c)


def test_sortinsert(s):
    print('#####################################')
    print('++++',s)
    sortinsert(s)
    print('++++',s)

def test_sortselect(s):
    print('#####################################')
    print('++++',s)
    sortselect(s)
    print('++++',s)


if __name__ == '__main__':
    ints1 = [i for i in range(20)]
    ints2 = [i for i in range(19,-1,-1)]
    test_sortinsert(ints1)
    test_sortinsert(ints2)

    ints1 = [i for i in range(20)]
    ints2 = [i for i in range(19, -1, -1)]
    test_sortselect(ints1)
    test_sortselect(ints2)

