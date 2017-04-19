# coding: utf-8

import paramiko


def remote_execute(remote_ip, user, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_ip, 22, user, passwd)
    print "{0} run command :".format(remote_ip), cmd
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout.read()
    ssh.close()


def copy_file_to(remote_ip, user, passwd, local_file_path, remote_file_path):
    ssh = paramiko.Transport(remote_ip, 22)
    ssh.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(ssh)
    print "{0} Local file:".format("127.0.0.1"), local_file_path
    print "{0} Remote file:".format(remote_ip), remote_file_path
    sftp.put(local_file_path, remote_file_path)
    sftp.close()
    ssh.close()


