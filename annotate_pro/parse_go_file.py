# coding: utf-8

import os
import pandas as pd


def parse_file_by_pandas(file_name):
    """
    small file parser use pandas
    :param file_name:
    :return:
    """
    table = pd.read_table(file_name, sep='\t', chunksize=2, engine='python')
    # print type(table)
    for chunk in table:
        # print "123", type(chunk)
        print chunk
        break


def parse_file_by_ori(file_name):
    """
    do not use pandas parse file
    :param file_name:
    :return:
    """
    res_pro_dic = {}
    for line in open(file_name, 'r').readlines():
        single_line_list = line.strip('\n').split('\t')
        write_record_in_dic(res_pro_dic, single_line_list[1], single_line_list[4])

    return res_pro_dic


def write_record_in_dic(src_dic, key, value):
    """
    write key-value into dic with inspection
    :param src_dic:
    :param key:
    :param value:
    :return:
    """
    if key in src_dic.keys():
        src_dic[key] += ("\t" + value)
    else:
        src_dic[key] = value


if __name__ == "__main__":
    # root = PathController.get_root_path()
    current_dir = os.getcwd()

    # os.path.dirname()
    # parse_file_by_pandas(current_dir + "\\" + "input_go_files\\bp.txt")
    tmp_dic = parse_file_by_ori(current_dir + "\\" + "input_go_files\\bp.txt")
    for key in tmp_dic.keys():
        print "%s:%r" % (key, tmp_dic[key])
