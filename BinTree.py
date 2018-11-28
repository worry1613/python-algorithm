# -*- coding: utf-8 -*-
# @创建时间 : 17/10/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class TreeNode(object):
    def __init__(self, el, parent=None, ltree=None, rtree=None):
        self.__elem = el
        self.__parent = parent
        self.__lchild = ltree
        self.__rchild = rtree


class BinTree(object):
    def __init__(self):
        self.__root = None

    def is_empty(self):
        """二叉树是否为空"""
        pass

    def num_nodes(self):
        """二叉树的结点个数"""
        pass

    def data(self):
        """取根结点的数据"""
        pass

    def left(self):
        """取左子树"""
        pass

    def right(self):
        """取右子树"""
        pass

    def set_left(self, l):
        """左子树赋值"""
        pass

    def set_right(self, r):
        """右子树赋值"""
        pass

    def forall(self,fn):
        """对于二叉树每个结点，依次调用fn函数"""
        pass

    def traverse(self):
        """遍历二叉树每个结点"""
        pass


