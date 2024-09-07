import multiprocessing

def startJarvis():
    from main import start
    start()

def listenHotWord():
    from engine.features import hotword
    hotword()

if __name__=="__main__":
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()
        