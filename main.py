from hashlib import sha256
from threading import Thread
import threading
import numpy as np
import time

def timer():
    start_time = time.time()
    while(True):
        if threading.active_count() == 2:
            break
    print("--- %s seconds ---" % (time.time() - start_time))


def slice_float(count: int):
    num = 26
    a = np.linspace(0, num, count+1, True, dtype=int)
    return a

def iterat(a, b):
    for i in range(a, b + 1):
        for j in range(97, 123):
            for k in range(97, 123):
                for l in range(97, 123):
                    for o in range(97, 123):
                        yield chr(i) + chr(j) + chr(k) + chr(l) + chr(o)

def thr_broot(dec, a: int = 0, b: int = 0, iii:int = -1):
    for i in iterat(a, b):
        str1 = sha256(i.encode('utf-8')).hexdigest()
        if str1 in dec:
            print(str(iii)+")итог: " + i)

if __name__ == '__main__':
    dec = [
        '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
        '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',  # apple
        '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',  # mmmmm
    ]
    count_threads = int(input("количество потоков = "))
    if count_threads == 1:
        thr_broot(dec, 97, 122)
    else:
        slices = slice_float(count_threads)

        for i in range(count_threads):
            th = Thread(target=thr_broot, args=(dec, slices[i] + 97, slices[i+1] + 97, i))
            th.start()
        thh = Thread(target=timer)
        thh.start()
