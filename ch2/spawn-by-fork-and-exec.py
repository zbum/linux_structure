#!/usr/bin/python3

import os

ret = os.fork()
if ret == 0:
    os.posix_spawn("/bin/echo", ["echo", "echo", "posix_spawn()로 생성되었습니다."], {})
elif ret > 0:
    print( "echo명령어를 생성했습니다.")

