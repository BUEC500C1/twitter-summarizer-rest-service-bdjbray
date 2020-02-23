import logging
import threading
import time
import twitter
import os

def thread_function(name):
    print(name)
    logging.info("Thread %s: starting", name)
    cmdmulti="python twitter.py "+str(name)+" /Users/brayb/Downloads/pythonws/ec500/homework1_2_4/background.PNG"
    os.system(cmdmulti)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    name_list=["KingJames","BarackObama","tim_cook"]
    for index in name_list:
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
