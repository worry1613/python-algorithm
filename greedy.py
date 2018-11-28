# -*- coding: utf-8 -*-
# @创建时间 : 28/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/
# 贪心算法


def broadcast():
    """
    https://blog.csdn.net/gooaaee/article/details/79631392
    集合覆盖问题，假设你办了个广播节目，要让全美50个州的听众都能收听到。为此你需要决定在哪些广播台播出，在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。
    贪婪算法作为近似算法，步骤如下：
    1. 选出这样一个广播台，即它覆盖了最多的未覆盖州。即便这个广播台覆盖了一些已覆盖的州，也没有关系。
    2. 重复第一步，直到覆盖了所有的州。

    覆盖最多优先策略
    """
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    final_stations = set()
    stations = {'kone': set(['id', 'nv', 'ut']), 'ktwo': set(['wa', 'id', 'mt']), 'kthree': set(['or', 'nv', 'ca']),
                'kfour': set(['nv', 'ut']), 'kfive': set(['ca', 'az'])}

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)

    print(final_stations)


def dispatcher():
    """
    区间调度问题
    结束时间优先的策略
    :return:
    """
    jobs = [(9, 10), (11, 12), (10, 11), (9.5, 10.5), (10.5, 11.5)]
    jobs.sort(key=lambda x: x[1])
    ret = []
    ls, le = 0, 0
    for i in range(len(jobs)):
        if jobs[i][1] > le and jobs[i][0] >= le:
            ret.append(jobs[i])
            le = jobs[i][1]
    print(ret)


def job_dispatcher():
    """
https://blog.csdn.net/niuniu0205/article/details/81449538
某工厂收到了n个产品的订单,这n个产品分别在A、B两个车间加工,并且必须先在A车间加工后才可以到B车间加工。
某个产品i在A、B两车间加工的时间分别为Ai、Bi。怎样安排这n个产品的加工顺序,才能使总的加工时间最短。
这里所说的加工时间是指：从开始加工第一个产品到最后所有的产品都已在A、B两车间加工完毕的时间。
Input
第一行仅—个数据n(0 < n < 1000),表示产品的数量。接下来n个数据是表示这n个产品在A车间加工各自所要的时间(都是整数)。
最后的n个数据是表示这n个产品在B车间加工各自所要的时间(都是整数)。
Output
第一行一个数据,表示最少的加工时间;第二行是一种最小加工时间的加工顺序。
Sample Input
5 3 5 8 7 10 6 2 1 4 9
Sample Output
34 1 5 4 2 3
    :return:

    A-B最小优先策略,?????不知道对不对，和网上的不一样
    """
    n = 5
    jobs = [(3,6),(5,2),(8,1),(7,4),(10,9)]
    # newjobs = sorted(jobs,key=lambda x:x[0]-x[1])                   #A-B最短优先策略
    newjobs = sorted(jobs,key=lambda x:x[1],reverse=True)         #B加工时间最长优先策略
    ret = sum([job[0] for job in newjobs])+newjobs[-1][1]
    print([jobs.index(nj)+1 for nj in newjobs])
    print(ret)


def min_delay():
    """
    https://blog.csdn.net/mmc2015/article/details/45461683
    一堆任务，每个任务有最晚完成时间di，和需要持续的时间ti。
    真实安排这些任务时，每个任务有真是的开始时间si和结束时间fi。称一个任务的延迟时间为fi-di。
    目的：找一个安排任务的方案，使所有任务的总的延迟最小。

    最早截止时间优先。
    :return:
    """
    pass


if __name__ == '__main__':
    # broadcast()
    # dispatcher()
    job_dispatcher()
    # min_delay()
