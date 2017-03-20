# coding: utf-8

import os
from Bio import SeqIO


def parse_fasta_use_bio(file_name):
    """
    parse fasta file by BioPython
    :param file_name:
    :return: a list , where sequence name in it.
    """
    pro_id_list = []
    for seq_record in SeqIO.parse(file_name, "fasta"):
        tmp_list = seq_record.id.strip('\n').split('|')
        pro_id_list.append(tmp_list[1])
        # break

    return pro_id_list


def extract_into_several_files(file_name):
    """
    extract uniprot_sprot.fasta every single sequence a file
    :param file_name:
    :return:
    """
    pass

if __name__ == "__main__":
    pass
    # current_dir = os.getcwd()
    # pro_list = parse_fasta_use_bio(current_dir + "\\" + "input_nr\\uniprot_sprot.fasta")
    # for i in pro_list:
    #     print i

