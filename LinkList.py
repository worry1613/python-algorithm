# -*- coding: utf-8 -*-
# @创建时间 : 28/9/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class LNode:
    """
    单链表结点类
    """
    def __init__(self, el, n=None):
        self.elem = el
        self.next = n

class LinkListError(ValueError):
    pass

class LList:
    """
    单向链表类
    """
    def __init__(self):
        """
        初始化
        """
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        """
        清空链表，删除所有节点
        :return:
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        链表是否为空,空true 非空 false
        :return:
        """
        return True if self.size else False

    def front(self):
        """
        返回第一个节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        return self.head

    def back(self):
        """
        返回最后一个节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        return self.tail

    def push_front(self,el):
        """
        在链表头插入一个新节点
        :return:
        """
        h = LNode(el)
        if not self.size:
            self.head = h
            self.tail = h
        else:
            h.next = self.head
            self.head = h
        self.size += 1

    def push_back(self,el):
        """
        在链表尾插入一个新节点
        :return:
        """
        h = LNode(el)
        if not self.size:
            self.head = h
            self.tail = h
        else:
            self.tail.next = h
            self.tail = h
        self.size += 1

    def pop_front(self):
        """
        删除链表头节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def pop_back(self):
        """
        删除链表尾节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            e = self.head
            while e.next and e.next is not self.tail:
                p = e.next
            self.tail = p
            self.tail.next = None
        self.size -= 1

    def delete(self,el):
        """
        删除指的一个节点
        :return:
        """
        pass

    def reverse(self):
        """
        反转链表
        :return:
        """
        h = self.head
        while True:
            pass

    def merge(self):
        """
        合并链表
        :return:
        """
        pass

    def size(self):
        """
        链表尺寸
        :return:
        """
        return self.size

    def swap(self):
        """
        链表交换
        :return:
        """
        pass

    def sort(self):
        """
        链表排序
        :return:
        """
        pass

    def get(self,i):
        """
        访问链表i位置的节点
        :return:
        """
        pass

    def elements(self):
        """
        遍历链表所有节点
        :return:
        """
        p = self.head
        while p.next:
            yield p.elem
            # print('el=%d, next=%d' % (p.elem, p.next),end='|')
            p = p.next





