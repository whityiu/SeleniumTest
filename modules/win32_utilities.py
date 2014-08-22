import win32api, win32pdhutil, win32con

def nuke_all_ie():
    try:
        win32pdhutil.FindPerformanceAttributesByName("Process", "ID Process", "iexplore")
    except:
        pass

    pids = win32pdhutil.FindPerformanceAttributesByName("iexplore")

    if len(pids) > 0:
        for p in pids:
            handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p)
            win32api.TerminateProcess(handle,0)
            win32api.CloseHandle(handle)