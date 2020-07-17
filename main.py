from time import sleep
import platform
import subprocess
from tripplite import PDU
import os

PDU_HOST = os.environ['PDU_HOST']
PDU_SOCKET = os.environ['PDU_SOCKET']
PDU_USERNAME = os.environ['PDU_USERNAME']
PDU_PASSWORD = os.environ['PDU_PASSWORD']
hostname = os.environ['HOST']

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def trigger_restart():
    print("RESTARTING...")    
    PDU().power_cycle(PDU_HOST, PDU_SOCKET, PDU_USERNAME, PDU_PASSWORD)
    
down_count = 0

while True:
    resp = ping(hostname)
    if resp == True:
        down_count = 0
    else:
        down_count += 1
    print('Current Count: %s' % down_count)

    if (down_count == 8):
        trigger_restart()

    sleep(15)
