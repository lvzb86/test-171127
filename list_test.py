# coding:utf-8

from timeit import Timer


def test1():    # 列表+操作
    l = []
    for i in range(1000):
        l += [i]


def test2():    # 向列表中追加列表
    l = []
    for i in range(1000):
        l.extend([i])


def test3():    # 向列表中不断追加元素
    l = []
    for i in range(1000):
        l.append(i)


def test4():    # 列表生成器
    l = [i for i in range(1000)]


def test5():    # 将可迭代对象直接转换成列表
    l = list(range(1000))


def test():
    t1 = Timer("test1()", "from __main__ import test1")
    print("list+=       ", t1.timeit(number=1000), "seconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print("extend()     ", t2.timeit(number=1000), "seconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print("append()     ", t3.timeit(number=1000), "seconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print("list[i]      ", t4.timeit(number=1000), "seconds")

    t5 = Timer("test5()", "from __main__ import test5")
    print("list range   ", t5.timeit(number=1000), "seconds")


if __name__ == '__main__':
    test()
