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
        self.val = el
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
        return True if not self.size else False

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
                e = e.next
            self.tail = e
            self.tail.next = None
        self.size -= 1

    def delete(self,el, pos):
        """
        删除指的一个节点el,或者删除指定位置pos的结点
        :return:
        """
        # if not self.size:
        #     #空链表，报错
        #     raise LinkListError('linklist is empty')
        # if self.size == 1 and self.head.val == el:
        #     self.head = None
        #     self.tail = None
        #     self.size -= 1
        # elif self.head.val == el:
        #     self.head = self.head.next
        #     self.size -= 1
        # else:
        #     e = self.head
        #     p = None
        #     while e :
        #         if e.val != el:
        #             p = e
        #             e = e.next
        #         else:
        #             p.next = e.next
        #             if e == self.tail:
        #                 self.tail = p
        #             self.size -= 1
        #             break
        if pos is None:
            if not self.head: return  # 空
            if self.head.val == el:  # 删除首结点的链表
                if not self.head.next:
                    self.head = None
                    self.size-=1
                    return
                else:
                    self.head = self.head.next
                    self.size -= 1
                    return
            cur, prev = self.head, self.head
            while cur.next:
                if el != cur.val:
                    prev = cur
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur.next = None
                    self.size -= 1
                    return
            if cur.val == el:
                prev.next = None
                self.size -= 1
                return
        else:
            #0<=pos,pos大于链表长度，直接返回
            n = 0
            if not self.head: return  # 空
            if pos ==0:  # 1个结点的链表
                if not self.head.next : self.head = None
                else: self.head = self.head.next
                self.size -= 1
                return
            elif pos == 1 and not self.head.next.next: #2个结点
                self.head.next = None
                self.size -= 1
                return
            cur = self.head
            next = self.head.next
            while next:
                if pos-1 != n:
                    cur = next
                    next = next.next
                else:
                    if not next.next:
                        cur.next = None
                    else:
                        cur.next = next.next
                    # cur.next = None
                    self.size -= 1
                    return
                n += 1

    def insert(self, pos=0, el=None):
        """
        在指定位置插入新节点
        pos 位置，从0开始
        :return:
        """
        # if isinstance(pos,int):
        #     if 0 > pos or pos > self.size:
        #         raise LinkListError('i is false %d' % (pos,))
        #     elif pos == 0:
        #         self.push_front(el)
        #     elif pos == self.size:
        #         self.push_back(el)
        #     else:
        #         count=0
        #         e = self.head
        #         while count != pos-1:
        #             e = e.next
        #             count+=1
        #         h = LNode(el)
        #         h.next = e.next
        #         e.next = h
        #         self.size += 1
        # else:
        #     raise LinkListError('param pos is not int type!!')
        n = 0
        e = LNode(el)
        if pos == 0:
            e.next = self.head
            self.head = e
            self.size += 1
            return
        cur,prev = self.head,None
        while cur:
            if pos-1 == n:
                e.next = cur.next
                cur.next = e
                self.size += 1
                return
            else:
                prev = cur
                cur = cur.next
                n += 1
        if pos >n or pos<0:    #pos<0 ,pos大于链表长度，加在链表尾部
            prev.next = e
            self.size += 1

    def reverse(self,dg=0):
        """
        反转链表
        dg 是否使用递归
        :return:
        """
        if self.size in [0, 1]:
            return self
        else:
            if dg:
                return self.__reverse(self.head)
            else:
                cur = self.head
                newhead = None
                next = None
                while cur:
                    next = cur.next
                    cur.next = newhead
                    newhead = cur
                    cur = next
                return newhead

    def __reverse(self,n):
        """
        反转链表,递归
        :return:
        """
        if n is None or n.next is None:
            return n
        else:
            newhead = self.__reverse(n.next)
            n.next.next = n
            n.next = None
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

    def length(self):
        """
        链表尺寸
        :return:
        """
        return self.size

    def swap(self,l):
        """
        链表交换
        :return:
        """
        self.head,self.tail,self.size,l.head,l.tail,l.size = \
            l.head,l.tail,l.length(),self.head,self.tail,self.length()

    def sort(self,flag=0):
        """
        链表排序
        flag        0 插入排序
                    1 快排
                    2 冒泡排序
        :return:
        """
        pass

    def get(self,i):
        """
        访问链表i位置的节点
        :return:
        """
        if isinstance(i,int):
            if not self.size:
                #空链表，报错
                raise LinkListError('linklist is empty')
            if 0 >= i or i > self.size:
                raise LinkListError('i is false %d' % (i,))
            n=0
            e = self.head
            while e.next and e.next is not self.tail and n != i:
                e = e.next
                n+=1
            return e.val
        else:
            raise LinkListError('param i is not int type!!')

    def valents(self):
        """
        遍历链表所有节点
        :return:
        """
        if not self.size:
            #空链表，报错
            raise LinkListError('linklist is empty')
        p = self.head
        while p is not None:
            yield p.val
            # print('el=%d, next=%d' % (p.val, p.next),end='|')
            p = p.next

    def isinList(self,el):
        """
        el是否在链表中
        :return:
        """
        if isinstance(el, int):
            if not self.size:
                #空链表，报错
                raise LinkListError('linklist is empty')
            p = self.head
            while p.val != el and p:
                p = p.next
            return True if p.val == el else False
        else:
            raise LinkListError('param el is not int type!!')



###############################################
# 测试
def printlist(l):
    les = None
    if isinstance(l,LList):
        try:
            les = [e for e in l.valents()]
            print(les, l.length())
        except Exception as e:
            print(e)
    elif isinstance(l,LNode):
        while l :
            print(l.val,end=', ')
            # print('el=%d, next=%d' % (p.val, p.next),end='|')
            l = l.next
        print()

if __name__ == '__main__':
    lempty = LList()
    lone = LList()
    lone.push_back(999)
    lone.push_back(10)
    # lone.push_back(1000)
    # test push_back
    # try:
    #     printlist(lempty)
    # except Exception as e:
    #     print(e)
    printlist(lone)

    l1 = LList()
    l2 = LList()
    for i in range(4):
        l1.push_back(i)
    l1.tail.next = l1.head
    s = set()
    c = l1.head
    while c:
        if c in s:
            print('hhhhhh')
            exit()
        else:
            s.add(c)
            c = c.next
    print('nnnnnn')
    exit()

    # for j in range(20,30):
    #     l2.push_back(j)
    # l1vals = [e for e in l1.valents()]
    # l2vals = [e for e in l2.valents()]
    printlist(l1)
    printlist(l2)

    lempty.delete(el=None,pos=0)
    printlist(lempty)

    lone.delete(el=None,pos=lone.length()-1)
    printlist(lone)
    lone.delete(el=None,pos=0)
    printlist(lone)
    # l1.delete(pos=999,el=None)
    # printlist(l1)
    # l1.delete(pos=0,el=None)
    # printlist(l1)
    # l1.insert(el=999,pos=0)
    # printlist(l1)
    # l1.insert(el=200,pos=200)
    # printlist(l1)
    # l1.insert(el=0,pos=110)
    # printlist(l1)
    # l1.insert(el=1,pos=1)
    # printlist(l1)
    # l1.insert(el=2,pos=2)
    # printlist(l1)
    # l1.insert(el=l1.length(),pos=l1.length()-1)
    # printlist(l1)
    # l1.delete(el=1, pos=None)
    # printlist(l1)
    # l1.delete(el=1, pos=None)
    # printlist(l1)
    # l1.delete(el=999, pos=None)
    # printlist(l1)
    # l1.delete(el=1, pos=None)
    # printlist(l1)
    # l1.delete(el=2, pos=None)
    # printlist(l1)
    # l1.delete(el=0, pos=None)
    # printlist(l1)
    # l1.insert(el=1, pos=1)
    # l1.insert(el=2, pos=2)
    # l1.insert(el=2, pos=2)
    # l1.insert(el=2, pos=2)
    # l1.insert(el=0, pos=0)
    # l1.insert(el=0, pos=0)
    # l1.insert(el=0, pos=0)
    # printlist(l1)
    l1.delete(el=None, pos=l1.length()-1)
    printlist(l1)
    l1.delete(el=None, pos=1)
    printlist(l1)

    l1.delete(el=None, pos=0)
    printlist(l1)
    l1.delete(el=None, pos=10)
    printlist(l1)
    l1.delete(el=None, pos=l1.length()-1)
    printlist(l1)
    # test is_empy
    # print('#####is_empty######')
    # print('lempty',lempty.is_empty())
    # print('lone',lone.is_empty())
    # print('l1',l1.is_empty())
    # print('l2',l2.is_empty())
    #
    # print('#####front######')
    # try:
    #     print('lempty', lempty.front())
    # except Exception as e:
    #     print('lempty ',e)
    # print('lone',lone.front().val)
    # print('l1',l1.front().val)
    # print('l2',l2.front().val)
    #
    # print('#####back######')
    # try:
    #     print('lempty', lempty.back())
    # except Exception as e:
    #     print('lempty ',e)
    # print('lone',lone.back().val)
    # print('l1',l1.back().val)
    # print('l2',l2.back().val)

    # print('#####get######')
    # try:
    #     print('lempty', lempty.get(None))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.get('a'))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.get(-100))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.get(100))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.get(0))
    # except Exception as e:
    #     print('lempty', e)
    #
    # try:
    #     print('lone',lone.get(None))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone',lone.get('a'))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone',lone.get(-100))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone',lone.get(100))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone',lone.get(1))
    # except Exception as e:
    #     print('lone', e)
    #
    #
    # try:
    #     print('l1',l1.get(None))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1',l1.get('a'))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1',l1.get(-100))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1',l1.get(100))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1',l1.get(1))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1',l1.get(10))
    # except Exception as e:
    #     print('l1', e)
    #
    # try:
    #     print('l2',l2.get(None))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2',l2.get('a'))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2',l2.get(-100))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2',l2.get(100))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2',l2.get(1))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2',l2.get(10))
    # except Exception as e:
    #     print('l2', e)


    # print('#####isinList######')
    # try:
    #     print('lempty', lempty.isinList(None))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.isinList('a'))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     print('lempty', lempty.isinList(-100))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     if lempty.head.val is not None:
    #         el = lempty.head.val
    #         print('lempty', lempty.isinList(el))
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     if lempty.tail.val is not None:
    #         el = lempty.tail.val
    #         print('lempty', lempty.isinList(el))
    # except Exception as e:
    #     print('lempty', e)
    #
    # try:
    #     print('lone', lone.isinList(None))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone', lone.isinList('a'))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     print('lone', lone.isinList(-100))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     if lone.head.val is not None:
    #         el = lone.head.val
    #         print('lone', lone.isinList(el))
    # except Exception as e:
    #     print('lone', e)
    # try:
    #     if lone.tail.val is not None:
    #         el = lone.tail.val
    #         print('lone', lone.isinList(el))
    # except Exception as e:
    #     print('lone', e)
    #
    # try:
    #     print('l1', l1.isinList(None))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1', l1.isinList('a'))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     print('l1', l1.isinList(-100))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     if l1.head.val is not None:
    #         el = l1.head.val
    #         print('l1', l1.isinList(el))
    # except Exception as e:
    #     print('l1', e)
    # try:
    #     if l1.tail.val is not None:
    #         el = l1.tail.val
    #         print('l1', l1.isinList(el))
    # except Exception as e:
    #     print('l1', e)
    #
    # try:
    #     print('l2', l2.isinList(None))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2', l2.isinList('a'))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     print('l2', l2.isinList(-100))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     if l2.head.val is not None:
    #         el = l2.head.val
    #         print('l2', l2.isinList(el))
    # except Exception as e:
    #     print('l2', e)
    # try:
    #     if l2.tail.val is not None:
    #         el = l2.tail.val
    #         print('l2', l2.isinList(el))
    # except Exception as e:
    #     print('l2', e)

    # print('#####push_front######')
    # elf = 1024
    # lempty.push_front(elf)
    # lone.push_front(elf)
    # l1.push_front(elf)
    # l2.push_front(elf)
    # printlist(lempty)
    # printlist(lone)
    # printlist(l1)
    # printlist(l2)
    #
    # print('#####push_back######')
    # elf = 1024
    # lempty.push_back(elf)
    # lone.push_back(elf)
    # l1.push_back(elf)
    # l2.push_back(elf)
    # printlist(lempty)
    # printlist(lone)
    # printlist(l1)
    # printlist(l2)
    #
    # print('#####pop_front######')
    # lempty.pop_front()
    # lone.pop_front()
    # l1.pop_front()
    # l2.pop_front()
    # printlist(lempty)
    # printlist(lone)
    # printlist(l1)
    # printlist(l2)
    # ################################
    # print('#####pop_back######')
    # lempty.pop_back()
    # lone.pop_back()
    # l1.pop_back()
    # l2.pop_back()
    # try:
    #     printlist(lempty)
    # except Exception as e:
    #     print('lempty', e)
    # printlist(lone)
    # printlist(l1)
    # printlist(l2)
    #
    # try:
    #     lempty.pop_front()
    # except Exception as e:
    #     print('lempty', e)
    # try:
    #     lempty.pop_back()
    # except Exception as e:
    #     print('lempty', e)
    #
    # print('#####delete######')
    # el = 999
    # try:
    #     lempty.delete(el)
    # except Exception as e:
    #     print('lempty', e)
    # lone.delete(el)
    # l1.delete(el)
    # l2.delete(el)
    # try:
    #     printlist(lempty)
    # except Exception as e:
    #     print('lempty', e)
    # printlist(lone)
    # l1.delete(0)
    # l1.delete(9)
    # l2.delete(20)
    # l2.delete(29)
    # printlist(l1)
    # printlist(l2)
    #
    # print('#####insert######')
    # el = 100
    # lempty.insert(el=el)
    # lone.insert(el=el)
    # l1.insert(el=el)
    # l2.insert(el=el)
    # l2.insert(2,el=el)
    # l2.insert(4,el=el+40)
    # l2.insert(6,el=el+60)
    #
    # printlist(lempty)
    # printlist(lone)
    # printlist(l1)
    # printlist(l2)
    #
    # print('#####swap######')
    # lempty.swap(l2)
    # l1.swap(lone)
    # l2.swap(l1)
    #
    # printlist(lempty)
    # printlist(l1)
    # printlist(l2)



    # print('#####reverse######')
    # ne = lempty.reverse()
    # nl = lone.reverse()
    # n1 = l1.reverse()
    # n2 = l2.reverse()
    #
    # printlist(ne)
    # printlist(nl)
    # printlist(n1)
    # printlist(n2)
    # # printlist(l2.reverse(dg=1))






