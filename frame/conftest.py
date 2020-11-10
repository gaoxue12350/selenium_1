import os
import signal
import subprocess
import pytest

@pytest.fixture(scope="module",autouse=True)
def record_vedio():
    #使用scrcpy录屏
    command="scrcpy --record tmp.mp4"
    p=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid, signal.SIGTERM)   #mac
    # os.kill(p.pid, signal.CTRL_C_EVENT)  #win