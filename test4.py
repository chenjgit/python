# 文件处理
# f=open('a1.txt','a')
# f=open('a1.txt','r')
# f=open('a1.txt','w')
# f=open('a1.txt','w+')
from fileinput import close
from unittest.mock import patch

# f=open('file/a3.txt', 'r')
# content=f.read()
# content=f.readline()
# content=f.readlines()
# print(content)
# model=f.mode
# name=f.name
# f.close()
# closed=f.closed

# c(content,name,model,closed)

import os
# os.rename('a22.txt','a2.txt')
# os.remove('a1.txt')
# 批量修改文件名称
# path=input('请输入文件路径: ')
# file_list=os.listdir(path)
# n=0
# for i in file_list:
#     oldname=path+os.sep+file_list[n]
#     newname=path+os.sep+'a'+str(n+1)+".txt"
#     os.rename(oldname,newname)
#     n=n+1


# 使用相对路径（更推荐，文件会保存在当前脚本所在目录）
# try:
#     # 相对路径：文件会创建在脚本所在的同一个文件夹
#     with open('a1.txt', 'a', encoding='utf-8') as f:
#         f.write('nihao\n')  # 加换行符，方便查看
#     print("写入成功！文件保存位置：")
#     import os
#     print(os.path.abspath('a1.txt'))  # 打印文件的绝对路径
# except PermissionError:
#     print("权限错误：无法写入文件，请检查路径或权限")
# except Exception as e:
#     print(f"发生错误：{e}")


# pandas处理excel
import pandas as pd
# sheet=pd.read_excel('example1.xlsx')
# sheet=pd.read_excel('excel_example.xlsx',sheet_name=[0,1])
# sheet=pd.read_excel('excel_example.xlsx',sheet_name=[1])
# sheet=pd.read_excel('excel_example.xlsx',skiprows=1)
# sheet=pd.read_excel('excel_example.xlsx',skipfooter=1)
# print(sheet)
# sheet=pd.read_csv('train.csv')
# print(sheet)
# 导出
# df=pd.DataFrame({
#     'id':[1,2,3],
#     'name':['zs','lisi','wangmazi']
# })
# df.to_excel('dctest.xlsx')
# 批量读取文件
import glob
path='three'
file=glob.glob(os.path.join(path,'*.csv'))
dl=[]
for i in file:
    dl.append(pd.read_csv(i))
print(dl)