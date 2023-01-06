import socketio

import os, errno
import win32pipe
import win32file
import pywintypes
import time

print("pipe client")
quit = False
output = []
while True:
    try:
        handle = win32file.CreateFile(
            r'\\.\pipe\Foo',
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )
        res = win32pipe.SetNamedPipeHandleState(
            handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
        if res == 0:
            print(f"SetNamedPipeHandleState return code: {res}")
        while True:
            output.clear()
            resp = win32file.ReadFile(handle, 64*1024)
            # print(resp,"\n")
            # print(f"message: {resp}\n")
            # resp=str(resp, 'utf-8')
            output.append(resp)

            print(output)
            
    except pywintypes.error as e:
        if e.args[0] == 2:
            print("no pipe, trying again in a sec")
            time.sleep(1)
        elif e.args[0] == 109:
            print("broken pipe, bye bye")
            quit = False
    # output=str(output)
    # substring = "0, b"
    # output_string = ""
    # str_list = output.split(substring)
    # for element in str_list:
    #     output_string += element
