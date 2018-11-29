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
    jobs = [(3, 6), (5, 2), (8, 1), (7, 4), (10, 9)]
    # newjobs = sorted(jobs,key=lambda x:x[0]-x[1])                   #A-B最短优先策略
    newjobs = sorted(jobs, key=lambda x: x[1], reverse=True)  # B加工时间最长优先策略
    ret = sum([job[0] for job in newjobs]) + newjobs[-1][1]
    print([jobs.index(nj) + 1 for nj in newjobs])
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
    jobs = [(2, 6), (3, 1), (1, 2)]  # (持续时间,最晚完成时间)
    newjobs = sorted(jobs, key=lambda x: x[1])  # 最早完成时间优先
    # newjobs = sorted(jobs,key=lambda x:x[0])        #最短持续时间优先
    ret, s, f = 0, 0, 0
    for i in range(len(newjobs)):
        s = f
        f += newjobs[i][0]
        if f > newjobs[i][1]:
            ret += (f - newjobs[i][1])
    print(newjobs)
    print(ret)


def multi_machine_dispatcher():
    """
    多机调度
    https://blog.csdn.net/hello_yz/article/details/8794843
    设有n个独立的作业，由m台相同的机器进行加工处理。作业i所需的处理时间为t[i]。
    任何作业可以在任何一台机器上面加工处理，但未完工之前不允许中断处理。任何作业不能拆分成更小的作业。
    要求给出一种作业调度方案，使所给的n个作业在尽可能短的时间内由m台机器加工处理完成。

    采用最长处理时间作业优先的贪心选择策略，可以设计出解多机调度问题较好的近似算法。

    最长处理时间作业优先
    :return:
    """
    machines = 3
    jobs = [16, 14, 6, 5, 4, 3, 2]
    machinesret = [0]*machines
    machinesd = [[] for _ in range(machines)]
    while jobs:
        m = max(jobs)
        mi = machinesret.index(min(machinesret))
        machinesd[mi]+=[m]
        machinesret[mi] += m
        jobs.remove(m)
    print(machinesret)
    print(machinesd)


def min_delay2():
    """
    https://bbs.csdn.net/topics/392290483
    总工件流水时间最小单机调度问题
    具体描述为20个工件需要在一台机器上加工完成，所有工件均在0时刻到达，其加工过程不可中断，且要求在其交货期前加工完成，
    各个工件的加工时间和交货期的数据如下表1所示。在这批工件加工过程中需要对这台设备进行两次预防性维护，每次设备维护的时长为1。
    表1：工件加工时间和交货期数据
    序号1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    加工时间1 3 3 3 3 3 3 4 4 4 4 4 5 5 5 6 6 6 7 7
    交货日期93 93 31 93 93 62 93 93 93 93 93 93 93 93 93 40 60 93 93 93

    子问题1.1：若设备预防性维护计划的开始时间分别设为：s1=29和s2=59，要求以总工件流水时间最小化为目标函数，求得上述工件的最优调度序列；
    子问题1.2：若设备预防性维护计划的开始时间分别设为：s1∈[25,35]和s2∈[55,65]，要求以总工件流水时间最小化为目标函数，
    求得上述工件的最优调度序列以及设备维护计划的最优开始时间，即和的最优值。
    提示：
    1）工件流水时间=等待时间+加工时间；
    2）若某一工件不能在设备维护开始前加工完成，则需要等待设备维护后才开始加工。
    :return:
    """
    pass


def job_dispatcher_discipline():
    """
    https://blog.csdn.net/WSYW126/article/details/51586443
    带惩罚的任务调度问题：
    单处理器上带截止时间和惩罚的单位时间任务调度问题有以下输入：
    1、n个单位时间任务的集合S={a1,a2,……,an}；
    2、n个整数截止时间d1,d2,……,dn，每个di满足1<=di<=n，我们期望任务ai在时间di之前完成。
    3、n个非负权重或者惩罚w1,w2,……,wn，若任务ai在时间di之前没有完成，我们就会受到wi这么多的惩罚，如果任务在截止时间之前完成，则不会受到惩罚。
    （单位时间任务是严格需要一个时间单位来完成的作业）
    在算法中我们定义延迟：如果方案中一个任务在截止时间后完成。都则就是提前。
    提前优先形式：将提前的任务都置于延迟任务之前。
    调度方案有规范形式：提前任务都在延迟任务之前，且提前任务按截止时间单调递增的顺序排列。

    :return:
    """
    pass


def tsp():
    """
    https://blog.csdn.net/DDelphine/article/details/51945265
    TSP问题
    旅行推销员问题（英语：Travelling salesman problem, TSP）是这样一个问题：给定一系列城市和每对城市之间的距离，
    求解访问每一座城市一次并回到起始城市的最短回路。它是组合优化中的一个NP困难问题，在运筹学和理论计算机科学中非常重要。
    :return:
    """
    pass


if __name__ == '__main__':
    # broadcast()
    # dispatcher()
    # job_dispatcher()
    # min_delay()
    multi_machine_dispatcher()
    min_delay2()
    job_dispatcher_discipline()
    tsp()
