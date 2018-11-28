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


if __name__ == '__main__':
    # broadcast()
    dispatcher()
