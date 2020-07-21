#!/usr/bin/pyhton3
# coding:utf-8
import threading
import time

def run():

    time.sleep(1)
    print("当前线程的名称：",threading.current_thread().name)
    time.sleep(1)



if __name__=='__main__':
    start_time=time.time()
    print("主线程",threading.current_thread().name)
    thread=[]
    for i in range(5):
        t=threading.Thread(target=run)
        t.start()
        thread.append(t)

    print("正在运行的线程list：",threading.enumerate())
    print("正在运行的线程数量：",threading.activeCount())