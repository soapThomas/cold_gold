# coding utf-8

import os
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

IP_LIST = ["10.141.211.66", "10.141.211.67", "10.141.211.68", "10.141.211.69"]


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


def deploy_fasta(ip):
    # scp_cmd = "scp -r {0}@{1}:{2} {3}".format(ROOT_USER, "10.141.211.65", REMOTE_FASTA_PATH, LOCAL_FASTA_PATH)
    # remote_execute(ip, ROOT_USER, ROOT_PASSWD, scp_cmd)
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_FASTA_PATH + FASTA_NAME, REMOTE_FASTA_PATH + FASTA_NAME)


def tar_fasta(ip):
    tar_cmd = "cd {0}; tar -xvf {1}".format(REMOTE_FASTA_PATH, FASTA_NAME)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, tar_cmd)


def exec_align(fasta_A, fasta_B, result_file):
    """

    :param fasta_A:
    :param fasta_B:
    :param result_file:
    :return:
    """
    cmd = 'cd {0}; nohup ./NWalign {1} {2} > {3} &'.format(REMOTE_FASTA_PATH, fasta_A, fasta_B, result_file)

    return cmd


def split_task(proteins, category):
    """

    :param proteins:
    :return:
    """
    file_path = LOCAL_FASTA_PATH + "output"  #out_put里存放55321条30%去重后的数据

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

    tar_cmd = 'tar -cvf {0} {1}'.format(LOCAL_FASTA_PATH + category + ".tar.gz", LOCAL_FASTA_PATH + category + "/")
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

if __name__ == "__main__":
    pass
    # print fetch_result("sample_1_2.txt")
    # print PathController.get_root_path()
    # split_task()
    # for i in IP_LIST:
    #     deploy_nwalign(i)
    #     deploy_fasta(i)
    #
    # time.sleep(1)
    #
    # for i in IP_LIST:
    #     tar_fasta(i)

