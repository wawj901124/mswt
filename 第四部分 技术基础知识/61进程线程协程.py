# #进程
# from multiprocessing import Process,freeze_support
# import time
#
# def foo(i):
#     print("This is Process", i)
#     time.sleep(1)
# def man():
#     for i in range(5):
#         p = Process(target=foo, args=(i,))
#         p.start()
#         p.join()
#
# if __name__ == '__main__':
#     freeze_support()
#     man()



# #线程
# import threading
#
# def show(i):
#     print('This is Thread',i)
#
# for i in range(5):
#     t = threading.Thread(target=show,args=(i,))
#     t.start()


#协程
import gevent

def foo():
    print("start_foo")
    gevent.sleep(2)
    print("end_foo")

def bar():
    print("star_bar")
    gevent.sleep(0)
    print("end_bar")

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
