# coding: utf-8

# import os
import platform
import datetime
from annotate_pro.parse_go_file import *
from nr_pro.tar_nr_pro import *
from lib.nwalign.exec_align import *
from lib.remote.remoter import *


if __name__ == "__main__":
    current_dir = os.getcwd()
    print platform.system()

    if "Windows" in platform.system():
        bp_txt = "\\annotate_pro\\input_go_files\\bp.txt"
        nr_fas = "\\nr_pro\\input_nr\\data_30.fasta"
        sample_text = "\\annotate_pro\\input_go_files\\sample.txt"
        sample_fas = "\\nr_pro\\input_nr\\sample.fasta"

    else:
        bp_txt = "/annotate_pro/input_go_files/bp.txt"
        nr_fas = "/nr_pro/input_nr/data_30.fasta"
        sample_text = "/annotate_pro/input_go_files/sample.txt"
        sample_fas = "/nr_pro/input_nr/sample.fasta"

    # first_part:
    tmp_dic = parse_file_by_ori(current_dir + bp_txt)
    # print tmp_dic

    pro_list = parse_fasta_use_bio(current_dir + nr_fas)
    # print pro_list
    #

    starttime = datetime.datetime.now()
    # count = 0
    # for i in pro_list:
    #     if i in tmp_dic.keys():
    #         # print i
    #         count += 1
    #         # print i
    # print count          # 2457
    # print len(tmp_dic)   # 15960
    # print len(pro_list)  # 55321
    # endtime = datetime.datetime.now()
    # print (endtime - starttime).seconds

    qualify_pro = []
    count_2 = 0
    for i in tmp_dic.keys():
        if i in pro_list:
            # print i
            qualify_pro.append(i)
            count_2 += 1
    print count_2

    endtime_2 = datetime.datetime.now()
    print (endtime_2 - starttime).seconds

    # qualify_pro = []
    print qualify_pro
    split_task(qualify_pro, "bp")
    # for i in qualify_pro:






    # second part
    # 10.141.211.65作为跳板机
    # remote_execute('10.141.211.66', 'root', 'qwdong123', 'mkdir test')
