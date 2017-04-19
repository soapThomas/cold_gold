# coding utf-8

import os, sys
from lib.remote.remoter import *


# FILE_PATH = os.getcwd() +
REMOTE_NWALIGN_PATH = "/home/thomas/packageNWalign"
ROOT_USER = "root"
ROOT_PASSWD = "qwdong123"

LOCAL_NWALIGN_FILE = "/home/thomas/NWalign"
REMOTE_NWALIGN_FILE = "/home/thomas/packageNWalign/NWalign"

LOCAL_FASTA_PATH = "/home/thomas/test"
REMOTE_FASTA_PATH = "/home/thomas/packageNWalign/fasta"

IP_LIST = ["10.141.211.66", "10.141.211.67", "10.141.211.68", "10.141.211.69"]


def deploy_nwalign(ip):

    # create nwalign dir
    mkdir_cmd = "mkdir -p {0}".format(REMOTE_NWALIGN_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, mkdir_cmd)

    # copy_file_to remote nwalign dir
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_NWALIGN_FILE, REMOTE_NWALIGN_FILE)

    # make nwalign executable
    chmod_cmd = "chmod +x {0}".format(REMOTE_NWALIGN_FILE)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, chmod_cmd)


def deploy_fasta(ip):
    scp_cmd = "scp -r {0} {1}@{2}:{3}".format(LOCAL_FASTA_PATH, ROOT_USER, ip, REMOTE_FASTA_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, scp_cmd)


def exec_align(fasta_A, fasta_B, result_file):
    """

    :param fasta_A:
    :param fasta_B:
    :param result_file:
    :return:
    """
    cmd = 'nohup ./NWalign {0} {1} > {2} &'.format(fasta_A, fasta_B, result_file)

    return cmd


def split_task():
    """

    :return:
    """
    file_path = "F:\\test"
    for parent, dirnames, filenames in os.walk(file_path):
        print filenames


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
    # print fetch_result("sample_1_2.txt")
    # print PathController.get_root_path()
    # split_task()
    for i in IP_LIST:
        deploy_nwalign(i)
        deploy_fasta(i)