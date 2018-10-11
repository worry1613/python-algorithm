# -*- coding: utf-8 -*-
# @创建时间 : 11/10/18 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class StackError(ValueError):
    pass


class Stack():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """栈是否为空，是空true"""
        return not self.__list

    def top(self):
        """取栈顶数据，不删除"""
        if self.__list:
            return self.__list[-1]
        else:
            raise StackError('Stack is empty')

    def push(self, elem):
        """压栈"""
        self.__list.append(elem)

    def pop(self):
        """出栈，删除栈顶数据"""
        if self.__list:
            self.__list.pop()
        else:
            raise StackError('Stack is empty')

    def size(self):
        """栈中数据个数"""
        return len(self.__list)

    def clear(self):
        """清空栈内所有数据"""
        self.__list = []

    def traverse(self, fn):
        """从栈底到栈顶，依次调用fn函数"""
        l = self.size()
        for i in range(0, l):
            fn(self.__list[i])


if __name__ == '__main__':
    s = Stack()
    for j in range(10):
        s.push(j)
    s.traverse(print)
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    s.push(200)
    print(s.top())
    print(s.size())
    print(s.is_empty())
    sempty = Stack()
    print(sempty.is_empty())
    try:
        print(sempty.top())
    except Exception as e:
        print(e)

    try:
        print(sempty.top())
    except Exception as e:
        print(e)

    for j in range(9):
        sempty.push(j + 2)
    sempty.traverse(print)
    sempty.clear()
    print(sempty.is_empty())


    def check_parens(s):
        """检查s中插号是否匹配"""
        parens = '()[]{}'
        open_par = '([{'
        close_par = {')': '(', ']': '[', '}': '{'}
        st = Stack()
        slen = len(s)
        i = 0
        for j in range(slen):
            if s[j] not in parens:
                j += 1
            elif s[j] in open_par:
                st.push((s[j], j))
            else:
                top = st.top()
                if close_par[s[j]] == top[0]:
                    print('插号匹配成功，第%d个和%d, %s%s!!' % (top[1], j, top[0], s[j]))
                    st.pop()
                else:
                    print('第%d个字符没有匹配插号，%s' % (j, s[j]))
                    # st.pop()
        while not st.is_empty():
            print('第%d个字符没有匹配插号，%s' % (st.top()[1], st.top()[0]))
            st.pop()


    text = """{[}"""
    check_parens(text)
