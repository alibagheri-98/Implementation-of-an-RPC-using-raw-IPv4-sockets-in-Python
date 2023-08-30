from threading import Thread

from server import Server

if __name__ == '__main__':
    s1 = Server("s1", "127.0.0.1", 8000)
    t = Thread(target=s1.serve_forever, args=())
    t.setDaemon = True
    t.start()

    s2 = Server("s2", "127.0.0.1", 8001)
    t = Thread(target=s2.serve_forever, args=())
    t.setDaemon = True
    t.start()
