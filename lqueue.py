# -*- coding: utf-8 -*-
# @创建时间 : 11/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
from LinkList import LList


class QueueError(ValueError):
    pass

class Queue(object):
    def __init__(self):
        """初始化，链表实现"""
        self.__list = LList()

    def enqueue(self,el):
        """入队"""
        self.__list.push_back(el)

    def dequeue(self):
        """出队"""
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

    def peek(self):
        """返回队头元素"""
        try:
            return self.__list.front()
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
    pass
    q = Queue()
    # for j in range(10):
    #     q.enqueue(j)
    try:
        q.traverse(print)
    except Exception as e:
        print(e)
    try:
        print('peek=', q.peek().elem)
    except Exception as e:
        print(e)
    print('size=', q.size())
    print('is_empty=', q.is_empty())
    try:
        q.dequeue()
    except Exception as e:
        print(e)
    try:
        print('peek=', q.peek().elem)
    except Exception as e:
        print(e)
    print('size=', q.size())
    try:
        q.traverse(print)
    except Exception as e:
        print(e)
    q.enqueue(100)
    try:
        print('peek=', q.peek().elem)
    except Exception as e:
        print(e)
    print('size=', q.size())
    try:
        q.traverse(print)
    except Exception as e:
        print(e)