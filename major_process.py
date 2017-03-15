# coding: utf-8

# from annotate_pro import parse_go_files
import os
# import annotate_pro as ap
# import nr_pro as nr
from annotate_pro.parse_go_file import *
from nr_pro.tar_nr_pro import *


if __name__ == "__main__":
    current_dir = os.getcwd()

    # os.path.dirname()
    # parse_file_by_pandas(current_dir + "\\" + "input_go_files\\bp.txt")
    tmp_dic = parse_file_by_ori(current_dir + "\\annotate_pro\\" + "input_go_files\\bp.txt")
    pro_list = parse_fasta_use_bio(current_dir + "\\nr_pro\\" + "input_nr\\uniprot_sprot.fasta")

    for i in pro_list:
        if i in tmp_dic.keys():
            print i