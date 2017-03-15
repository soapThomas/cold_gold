# coding: utf-8

# import os
import platform
from annotate_pro.parse_go_file import *
from nr_pro.tar_nr_pro import *
from lib.remote.remoter import *


if __name__ == "__main__":
    current_dir = os.getcwd()
    print platform.system()
    # if "Windows" in platform.system():
    #     bp_txt = "\\annotate_pro\\input_go_files\\bp.txt"
    #     nr_fas = "\\nr_pro\\input_nr\\uniprot_sprot.fasta"
    # else:
    #     bp_txt = "/annotate_pro/input_go_files/bp.txt"
    #     nr_fas = "/nr_pro/input_nr/uniprot_sprot.fasta"
    #
    # # parse_file_by_pandas(current_dir + "\\" + "input_go_files\\bp.txt")
    # tmp_dic = parse_file_by_ori(current_dir + bp_txt)
    # pro_list = parse_fasta_use_bio(current_dir + nr_fas)
    #
    # count = 0
    # for i in pro_list:
    #     if i in tmp_dic.keys():
    #         count += 1
    #         # print i
    # print count
    # print len(tmp_dic)
    # print len(pro_list)

    # second part
    # 10.141.211.65作为跳板机
    remote_execute()
