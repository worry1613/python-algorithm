# -*- coding: utf-8 -*-
# @创建时间 : 11/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
from LinkList import LList
from lqueue import QueueError


class Deque(object):
    def __init__(self):
        """初始化，链表实现"""
        self.__list = LList()

    def push_back(self,el):
        """队尾入队"""
        self.__list.push_back(el)

    def push_front(self,el):
        """队头入队"""
        self.__list.push_front(el)

    def pop_back(self):
        """队尾出队"""
        try:
            self.__list.pop_back()
        except Exception as e:
            raise QueueError(e.args[0])

    def pop_front(self):
        """队头出队"""
        try:
            self.__list.pop_front()
        except Exception as e:
            raise QueueError(e.args[0])

    def is_empty(self):
        """队列是否为空"""
        return self.__list.is_empty()

    def size(self):
        """队列尺寸"""
        return self.__list.length()

    def front(self):
        """返回队头元素"""
        try:
            return self.__list.front()
        except Exception as e:
            raise QueueError(e.args[0])

    def back(self):
        """返回队尾元素"""
        try:
            return self.__list.back()
        except Exception as e:
            raise QueueError(e.args[0])

    def traverse(self,fn):
        """从队头到队尾，依次调用fn函数"""
        try:
            head = self.__list.front()
            while head:
                fn(head.elem)
                head = head.next
        except Exception as e:
            raise QueueError(e.args[0])


if __name__ == '__main__':
    q = Deque()

    try:
        q.traverse(print)
    except Exception as e:
        print(e)
    print('size=', q.size())
    print('is_empty=', q.is_empty())
    try:
        print('front=', q.front().elem)
    except Exception as e:
        print(e)
    try:
        print('back=', q.back().elem)
    except Exception as e:
        print(e)
    try:
        q.pop_back()
    except Exception as e:
        print(e)
    try:
        q.pop_front()
    except Exception as e:
        print(e)

    for j in range(10):
        q.push_back(j)
    try:
        q.traverse(print)
    except Exception as e:
        print(e)
    try:
        print('front=', q.front().elem)
    except Exception as e:
        print(e)
    try:
        print('back=', q.back().elem)
    except Exception as e:
        print(e)
    print('size=', q.size())

    el = 999
    q.push_back(el)
    q.push_front(el)
    try:
        print('front=', q.front().elem)
    except Exception as e:
        print(e)
    try:
        print('back=', q.back().elem)
    except Exception as e:
        print(e)
    print('size=', q.size())
    try:
        q.pop_back()
    except Exception as e:
        print(e)
    try:
        q.pop_front()
    except Exception as e:
        print(e)
    print('size=', q.size())
    try:
        q.traverse(print)
    except Exception as e:
        print(e)
    try:
        print('front=', q.front().elem)
    except Exception as e:
        print(e)
    try:
        print('back=', q.back().elem)
    except Exception as e:
        print(e)

