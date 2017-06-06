# coding: utf-8

import os
import time
from lib.remote.remoter import *


# FILE_PATH = os.getcwd() +
REMOTE_NWALIGN_PATH = "/home/thomas/packageNWalign"
ROOT_USER = "root"
ROOT_PASSWD = "qwdong123"

LOCAL_NWALIGN_FILE = "/home/thomas/NWalign"
REMOTE_NWALIGN_FILE = "/home/thomas/packageNWalign/NWalign"

LOCAL_FASTA_PATH = "/home/thomas/"
REMOTE_FASTA_PATH = "/home/thomas/packageNWalign/"
FASTA_NAME = "test.tar.gz"
SPLIT_FILE_NAME = "split.sh"
EXEC_FILE_NAME = "exec.sh"

IP_LIST = ["10.141.211.64", "10.141.211.66", "10.141.211.67", "10.141.211.68", "10.141.211.69"]


def deploy_nwalign(ip):

    rmdir_cmd = "rm -rf {0}".format(REMOTE_NWALIGN_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, rmdir_cmd)

    # create nwalign dir
    mkdir_cmd = "mkdir -p {0}".format(REMOTE_NWALIGN_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, mkdir_cmd)

    # copy_file_to remote nwalign dir
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_NWALIGN_FILE, REMOTE_NWALIGN_FILE)

    # make nwalign executable
    chmod_cmd = "chmod +x {0}".format(REMOTE_NWALIGN_FILE)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, chmod_cmd)


def deploy_fasta(ip, fasta_name):
    # scp_cmd = "scp -r {0}@{1}:{2} {3}".format(ROOT_USER, "10.141.211.65", REMOTE_FASTA_PATH, LOCAL_FASTA_PATH)
    # remote_execute(ip, ROOT_USER, ROOT_PASSWD, scp_cmd)
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_FASTA_PATH + fasta_name, REMOTE_FASTA_PATH + fasta_name)


def tar_fasta(ip, tar_name):
    tar_cmd = "cd {0}; tar -xvf {1}".format(REMOTE_FASTA_PATH, tar_name)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, tar_cmd)


def deploy_sh(ip, sh_name):
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_FASTA_PATH + sh_name, REMOTE_FASTA_PATH + sh_name)

    chmod_cmd = "chmod +x {0}".format(REMOTE_FASTA_PATH + sh_name)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, chmod_cmd)


def pre_exec_align(ip, count, i, threads):
    rmdir_cmd = "rm -rf {0}".format(REMOTE_NWALIGN_PATH + "/data")
    print rmdir_cmd
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, rmdir_cmd)

    begin = 1 + count / threads * i
    if i == threads - 1:
        end = count + 1
    else:
        end = begin + count / threads
    cmd = 'cd {0}; nohup ./{1} {2} {3} {4} &'.format(REMOTE_FASTA_PATH, "split.sh", "bp", begin, end)
    print cmd
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)


def exec_align(ip, source, desc):
    rmdir_cmd = "rm -rf {0}".format(REMOTE_NWALIGN_PATH + "/result")
    print rmdir_cmd
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, rmdir_cmd)

    cmd = 'cd {0}; nohup ./{1} {2} {3} > nohup.out &'.format(REMOTE_FASTA_PATH, "exec.sh", source, desc)
    print cmd
    remote_execute_none_read(ip, ROOT_USER, ROOT_PASSWD, cmd)


def split_task(proteins, category):
    """

    :param proteins:
    :return:
    """
    file_path = LOCAL_FASTA_PATH + "output"  # output里存放55321条30%去重后的数据

    rmdir_cmd = "rm -rf {0}".format(LOCAL_FASTA_PATH + category)
    os.system(rmdir_cmd)

    rmfile_cmd = "rm -rf {0}".format(LOCAL_FASTA_PATH + category + ".tar.gz")
    os.system(rmfile_cmd)

    mkdir_cmd = "mkdir -p {0}".format(LOCAL_FASTA_PATH + category + "/")
    os.system(mkdir_cmd)
    # print file_path
    for parent, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            filename_list = filename.split("_")
            pro_name = filename_list[1]
            if pro_name in proteins:
                cp_cmd = 'cp {0} ../{1}'.format(file_path+'/'+filename, category)
                # print cp_cmd
                os.system(cp_cmd)

    tar_cmd = 'cd {0}; tar -czf {1} {2}'.format(LOCAL_FASTA_PATH, category + ".tar.gz", category)
    print tar_cmd
    os.system(tar_cmd)


def fetch_result(file_name):
    """
    :param file_name
    :return:
    """
    for line in open(file_name, 'r').readlines():
        if line.startswith("Sequence identity"):
            single_line_list = line.strip('\n').split(' ')
            identity = single_line_list[1].split('=')
    return identity[1]


def test_nohup(ip, source, desc):

    cmd = 'cd {0}; nohup ./{1} {2} {3} > nohup.out &'.format(REMOTE_FASTA_PATH, "test.sh", source, desc)
    print cmd
    remote_execute_none_read(ip, ROOT_USER, ROOT_PASSWD, cmd)

if __name__ == "__main__":
    test_nohup(IP_LIST[0],  "bp", "data")
    test_nohup(IP_LIST[1], "bp", "data")
    # pass
    # print fetch_result("sample_1_2.txt")
    # print PathController.get_root_path()
    # split_task()
    # for i in IP_LIST:
    #     deploy_nwalign(i)
    #     deploy_fasta(i, "bp.tar.gz")

    # time.sleep(1)

    # for i in IP_LIST:
    #     tar_fasta(i, "bp.tar.gz")
    #     deploy_sh(i, SPLIT_FILE_NAME)


