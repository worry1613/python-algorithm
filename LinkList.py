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
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        if self.size == 1 and self.head.elem == el:
            self.head = None
            self.tail = None
        elif self.head.elem == el:
            self.head = self.head.next
        else:
            e = self.head
            while e.next and e.next is not self.tail and e.elem != el:
                e = e.next
            self.tail = e
            self.tail.next = None
        self.size -= 1

    def reverse(self):
        """
        反转链表
        :return:
        """
        h = self.head
        newhead = None
        pp = None
        pn = None
        if self.size in [0,1]:
            return self.head
        while h.next is not None:
            pn = h.next
            if pn is None:
                newhead = pn
                break
            pn.next = pp
            pp = h
            h = pn
        return newhead

    def merge(self,l1,l2):
        """
        合并链表
        :return:
        """
        if not l1.size():
            if not l2.size():
                pass
            else:
                l1.head = l2.head
                l1.tail = l2.tail
                l1.size = l2.size
        else:
            l1.tail.next = l2.head
            l1.tail = l2.tail
            l1.size +=l2.size

    def size(self):
        """
        链表尺寸
        :return:
        """
        return self.size

    def swap(self,l1,l2):
        """
        链表交换
        :return:
        """
        l1.head,l1.tail = l2.head,l2.tail

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
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        if 0 >= i > self.size:
            raise LinkListError('i is false')
        n=0
        e = self.head
        while e.next and e.next is not self.tail and n != i:
            e = e.next
            n+=1
        return e.elem

    def elements(self):
        """
        遍历链表所有节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        p = self.head
        while p.next:
            yield p.elem
            # print('el=%d, next=%d' % (p.elem, p.next),end='|')
            p = p.next

    def isinList(self,el):
        """
        el是否在链表中
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        p = self.head
        while p.elem != el:
            p = p.next
        return True if p.elem == el else False


# 测试
if __name__ == '__main__':
    l1 = LList()
    l2 = LList()
    for i in range(20):
        l1.push_back(i)
    for j in range(30,50):
        l2.push_back(j)
    l1elems = [e for e in l1.elements()]
    l2elems = [e for e in l2.elements()]


