import os
import sys


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

def get_filepath_shotname_extension(filename):
    (filepath, tempfilename) = os.path.split(filename)
    (shotname, extension) = os.path.splitext(tempfilename)
    # print("filepath: %s, shotname: %s, extension: %s"%(filepath, shotname, extension))
    return (shotname, extension)

import shutil
def copy_file_rename(filename):
    targetFileName = get_filepath_shotname_extension(filename)
    new_fileName = targetPath+"\\unit_env.md"
    old_fileName = curPath+"\\unit_env.md"
    shutil.copyfile(old_fileName, new_fileName)
    os.rename("unit_env", targetFileName[0])
    print(targetFileName[0])

if __name__ == "__main__":
    curPath = os.getcwd()
    tempPath = 'newFolder'
    targetPath = curPath+os.path.sep+tempPath
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    else:
        print('路径已经存在')
    file_list = os.listdir(curPath)
    map(copy_file_rename, file_list)