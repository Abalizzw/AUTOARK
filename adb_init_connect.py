import os
import adb_name

def initial_adb():
    cmd_kill = '{name} kill-server'.format(name=adb_name.adbname())
    cmd_connect = '{name} connect 127.0.0.1:7555'.format(name=adb_name.adbname())

    os.system(cmd_kill)
    os.system(cmd_connect)

if __name__=='__main__':
    initial_adb()
