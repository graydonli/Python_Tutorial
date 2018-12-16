#-*-coding:utf-8-*-

""" 
1. 将模板env文件拷贝到新建文件夹中
2. 拷贝旧文件的中间部分内容（描述，特性...），插入到新建文件夹中的模板文件env
3. 替换模板文件env中的unit名字为旧文件的，替换“购买链接”为速卖通，删除多余旧文件拷贝过来的“原理图”“购买链接”
4. 把改好的文件重命名，再拷贝到上一层目录中替换旧文件
"""


import os
import sys
import re


# def generate_files_path(dir_path):
#     # for root, dirs, files in os.walk(dir_path):
#     #     print(root, dirs, files)
#         # for i in files:
#         #     print(os.path.join(root, i))
#     print(os.listdir(dir_path))



# if __name__=='__main__':
#     # generate_files_path('E:\\product_pics_home_page\\docs\\assets\\img\\product_pics\\pictures_for_homepage\\units')
#     print(os.getcwd())

# curPath = os.getcwd()
# tempPath = 'newFolder'
# targetPath = curPath+os.path.sep+tempPath
# if not os.path.exists(targetPath):
#     os.makedirs(targetPath)
# else:
#     print('路径已经存在')
# file_list = os.listdir(curPath)
# file_count = len(file_list)
# for i in range(1,file_count+1):
#     print(i)
# print(type(range(1,10)))

curPath = os.getcwd()
newFolderName = 'newFolder'
file_list = []# 保存所有文件到这个列表中
    flag_find_desc = 0
    flag_find_picture = 0
    flag_file_exit_picture = 0
    pattern_desc = re.compile(r'## 描述')
    pattern_picture = re.compile(r'<figure>')
    pattern_example = re.compile(r'## 例程')
    pattern_purchase = re.compile(r'(\[购买链接\])\((.*?)\)')
    pos_example = 0
    count = 0
    count_example = 0
    data_to_write = []
    link_list = []

def newFolder(path, newFolderName):
    targetPath = curPath+os.path.sep+newFolderName
if not os.path.exists(targetPath):
    os.makedirs(targetPath)
else:
    print('路径已经存在')
# file_list = os.listdir(curPath)
# print(file_list)
# print("length of file_list: %d"%(len(file_list)))

def getAllFileName(path):
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i): 
            # recurseDir(path+'\\'+i) # 注释这条语句，不处理目录
            print("dir: %s"%(path+'\\'+i))
        else:
            p=path+'\\'+i
            # print(p)
            file_list.append(p)# 把所有文件都放进这个列表中保存

def get_filepath_shotname_extension(filename):
    (filepath, tempfilename) = os.path.split(filename)
    (shotname, extension) = os.path.splitext(tempfilename)
    # print("filepath: %s, shotname: %s, extension: %s"%(filepath, shotname, extension))
    return (shotname, extension)

import shutil
# def copyFileToTargetPath(old_file, TargetPath): # 绝对路径
    # targetFileName = get_filepath_shotname_extension(filename)
    # new_fileName = targetPath+"\\unit_env.md"
    # old_fileName = curPath+"\\unit_env.md"
    shutil.copyfile(old_fileName, new_fileName)# 拷贝文件
    # os.chdir(targetPath)
    # os.rename("unit_env.md", filename)# 重命名文件
    # print(targetFileName[0])
    # os.chdir(curPath)

def extract_content(filename):
    # filename = get_filepath_shotname_extension(filename)
    with open(filename,"r",encoding="utf-8") as f_r:
        for line in f_r.readlines():
            match_desc = pattern_desc.match(line)
            match_picture = pattern_picture.match(line)
            if match_desc or match_picture:
                if match_desc:
                    flag_find_desc = 1
                if match_picture:
                    flag_find_picture = 1
            if flag_find_picture: # end
                flag_file_exit_picture = 1
                flag_find_picture = 0
                flag_find_desc = 0
                # print(count)
                f_r.close()
            if flag_find_desc:
                data_to_write.append(line)
            count+=1
        if flag_file_exit_picture:
            flag_file_exit_picture = 0
        else: # this file doesn't have pictures
            # print("this file doesn't have pictures:  %s"%filename)
            flag_find_desc = 0
            f_r.close()
    # print(data_to_write)
    os.chdir(targetPath)
    with open("temp.md","w",encoding="utf-8") as temp_f_w:
        for i in data_to_write:
            temp_f_w.write(i)# 保存要拷贝的内容到临时文件中
    temp_f_w.close()

def add_data_to_file(des_file, src_file):# 插入到中文文件
    fp = open(des_file, "r", encoding="utf-8")
    fp_add = open(src_file,"r", encoding="utf-8")
    content = fp.read()
    content_add = fp_add.read()
    fp.close()
    fp_add.close()
    post = content.find("## 例程")# 寻找待插入位置所在的字符串
    if post != 1:
        content = content[:post] + content_add + content[post:]
        # print(content)
        fp = open(des_file, "w", encoding="utf-8")
        fp.write(content)
        fp.close()

def delect_replace_content(filename):
    """ 
    先通过正则表达式匹配出两个网址，然后将第一个匹配到的网址替换成第二个网址
    替换文件中的内容为对应unit名字
    删除多余的内容
    """
    filename = get_filepath_shotname_extension(filename)
    with open("1.md","r",encoding="utf-8") as fp:
        lines = fp.readlines()
        for line in lines:
            match_purchase = pattern_purchase.search(line)
            if match_purchase:
                link_list.append(match_purchase.group(2))
        # print(link_list)
    with open("1.md","w",encoding="utf-8") as f_w:
        for line in lines:
            if "ENV" in line:
                line = line.replace("ENV", "DAC")
            if "env" in line:
                line = line.replace("env", "dac")
            if link_list[0] in line:
                line = line.replace(link_list[0], link_list[1])
            if ("-  **例程**" or "- **例程**") in line:
                print(line)
                continue # 删除多余的
            if ("-  **[购买链接]" or "- **[购买链接]") in line:
                print(line)
                continue # 删除多余的
            f_w.write(line)    
    fp.close()
    f_w.close()

if __name__ == "__main__":
    # for i in file_list:
    #     if file_list[i]==""
    #     print(file_list[i])
    # copy_file_rename(file_list[2])
    # copy_file_rename(file_list[3])
    # map(copy_file_rename, file_list)

    os.chdir(targetPath)









