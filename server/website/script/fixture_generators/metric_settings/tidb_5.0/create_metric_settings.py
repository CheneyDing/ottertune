#
# Created on July 19, 2021
#
# @author: Yiqin Xiong
#

# TODO: 仿照oracle和postgres，从导出的metrics定义文件（oracle是json，postgres是csv，当然也可以自己定义metrics），转换为标准的metrics的json文件，拷贝到fixture目录中
# NOTE：当然也可以参考sap hana的添加：https://github.com/cmu-db/ottertune/pull/194/commits/10bdc3d378cf7c78110702dd85e317aa875ecf17
# NOTE：流程大概是 1.导出的metrics定义文件通过本文件得到fixture目录下标准的metrics的json文件 2.
