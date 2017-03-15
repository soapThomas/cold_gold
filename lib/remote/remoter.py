# coding: utf-8

import paramiko


def remote_execute(remote_ip, user, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_ip, 22, user, passwd)
    print "{0} run command :".format(remote_ip), cmd
    ssh.exec_command(cmd)
    ssh.close()

