from UnityTab import UnityTab
from UnityTab import Update
from TkinterTab import TkinterTab
import threading

tk = TkinterTab()

def threadmain():
    TkinterTab.mainloop(tk)


t = threading.Thread(target=threadmain)
t.start()

up = Update()
up.start()

