# -*- coding: utf-8 -*-
# @创建时间 : 11/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
from LinkList import LNode
from stack import StackError


class LStack():
    """链表实现栈"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """栈是否为空，是空true"""
        return not self.__head

    def top(self):
        """取栈顶数据，不删除"""
        if self.__head:
            return self.__head
        else:
            raise StackError('Stack is empty')

    def push(self, elem):
        """压栈"""
        self.__head = LNode(elem, self.__head)

    def pop(self):
        """出栈，删除栈顶数据"""
        if self.__head:
            self.__head = self.__head.next
        else:
            raise StackError('Stack is empty')

    def size(self):
        """栈中数据个数"""
        e = self.__head
        c = 0
        while e:
            c += 1
            e = e.next
        return c

    def clear(self):
        """清空栈内所有数据"""
        self.__head = None

    def traverse(self, fn):
        """从栈底到栈顶，依次调用fn函数"""
        self.__traverse(print, self.__head)

    def __traverse(self, fn, elem):
        if not elem:
            return
        self.__traverse(fn, elem.next)
        fn(elem.elem)


if __name__ == '__main__':
    s = LStack()
    for j in range(10):
        s.push(j)
    s.traverse(print)
    print('top=', s.top().elem)
    s.pop()
    print('top=', s.top().elem)
    s.pop()
    print('top=', s.top().elem)
    s.push(200)
    print('top=', s.top().elem)
    print('size=', s.size())
    print('is_empty=', s.is_empty())
    sempty = LStack()
    print(sempty.is_empty())
    try:
        print(sempty.top().elem)
    except Exception as e:
        print(e)

    try:
        print(sempty.top().elem)
    except Exception as e:
        print(e)

    for j in range(9):
        sempty.push(j + 2)
    sempty.traverse(print)
    sempty.clear()
    print('is_empty=', sempty.is_empty())
