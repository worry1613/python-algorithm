# -*- coding: utf-8 -*-
# @创建时间 : 11/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

from Dlinklist import DLList
from lqueue import QueueError

class PriorityDeque(object):
    def __init__(self):
        """初始化，双向链表实现，出队，入队时间都是O(1)"""
        self.__list = DLList()
        self.__pri = 0              #优先级,0最低优先级
        self.__high_pri = 0         #最高优先级
        self.__low_pri = 0          #最低优先级
        self.__pris = []            #保存所有优先级开始位置的数组，格式 (优先级,优先级开始元素)

    def push(self,el,pri=0):
        """入队"""
        self.__list.push_back(el)

    def pop(self):
        """出队"""
        try:
            self.__list.pop_back()
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
    d1 = DLList()
    d2 = DLList()
    d = {}
    key = 1000
    if key in d.keys():
        #已经有这个优先级的元素存在了
        pass
    else:
        #还没有这个优先级的元素存在
        d[key] = [d1,d2]


    # {1000:(d1,d2),300:(d1,d2),304:(d1,d2),1300:(d1,d2),3200:(d1,d2),30:(d1,d2),100:(d1,d2),2300:(d1,d2)}
    # print(d)
    #
    # if key in d.keys():
    #     print(key)
    # else:


    # q = Deque()
    #
    # try:
    #     q.traverse(print)
    # except Exception as e:
    #     print(e)
    # print('size=', q.size())
    # print('is_empty=', q.is_empty())
    # try:
    #     print('front=', q.front().elem)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('back=', q.back().elem)
    # except Exception as e:
    #     print(e)
    # try:
    #     q.pop_back()
    # except Exception as e:
    #     print(e)
    # try:
    #     q.pop_front()
    # except Exception as e:
    #     print(e)
    #
    # for j in range(10):
    #     q.push_back(j)
    # try:
    #     q.traverse(print)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('front=', q.front().elem)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('back=', q.back().elem)
    # except Exception as e:
    #     print(e)
    # print('size=', q.size())
    #
    # el = 999
    # q.push_back(el)
    # q.push_front(el)
    # try:
    #     print('front=', q.front().elem)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('back=', q.back().elem)
    # except Exception as e:
    #     print(e)
    # print('size=', q.size())
    # try:
    #     q.pop_back()
    # except Exception as e:
    #     print(e)
    # try:
    #     q.pop_front()
    # except Exception as e:
    #     print(e)
    # print('size=', q.size())
    # try:
    #     q.traverse(print)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('front=', q.front().elem)
    # except Exception as e:
    #     print(e)
    # try:
    #     print('back=', q.back().elem)
    # except Exception as e:
    #     print(e)

