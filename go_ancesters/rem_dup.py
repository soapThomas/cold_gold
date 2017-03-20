# coding: utf-8


def processFile(FILE_NAME):
    """
    remove res_bp -> out_res_bp.txt
    :param FILE_NAME:
    :return:
    """
    fr = open(FILE_NAME)
    fw = open('out' + FILE_NAME, 'w')
    for line in fr:
        duplicated_list = []
        lines = list(map(str, line.strip('\n').split('\t')))
        lines = lines[:-1]
        for i in lines:
            if i not in duplicated_list:
                duplicated_list.append(i)
                fw.write(str(i) + "\t")
        fw.write("\n")
    fr.close()
    fw.close()


if __name__ == '__main__':
    processFile('res_bp.txt')
    processFile('res_mf.txt')
    processFile('res_cc.txt')
