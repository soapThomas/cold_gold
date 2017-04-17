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
    