# cold_gold

*------------------------*
原始GO注释数据集1：annotate_pro\input_go_files目录下
bp.txt
cc.txt
mf.txt

分别是从Go annation中分类筛选出来的 三类evidence code为exp、并且数据库是UniProtKB的结果
每个文件有两列有用，分别是蛋白质和GO项
*------------------------*


*+++++++++++++++++++++++++*
原始蛋白质序列数据集2: nr_pro\input_nr目录下
uniprot_sprot.fasta 未去重的数据

去重命令：
cd-hit -i uniprot_sprot.fasta -o nr_90.fasta -c 0.9 -n 5
cd-hit -i nr_90.fasta -o nr_60.fasta -c 0.6 -n 4
./psi-cd-hit.pl -i ../nr_60.fasts -o nr_30.fasta -c 0.3
*+++++++++++++++++++++++++*


*··························*
配置相关信息：
10.141.211.65 上作为跳板机，用来控制66-69的蛋白质比对，ioncom比对，nwalign比对
10.141.211.66 上存放着ioncom /mnt目录下
10.141.211.69 上存放着cd-hit 百分之30去重之后的结果
*··························*
