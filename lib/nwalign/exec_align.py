# coding utf-8

from lib.remote.remoter import *


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
    pass


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
    print fetch_result("sample_1_2.txt")