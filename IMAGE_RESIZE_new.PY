from PIL import Image
import os

cur_path = os.getcwd()

def get_filepath_shotname_extension(filename):
    (filepath, tempfilename) = os.path.split(filename)
    (shotname, extension) = os.path.splitext(tempfilename)
    # print("filepath: %s, shotname: %s, extension: %s"%(filepath, shotname, extension))
    return (shotname, extension)

def image_resize(file_dir):
    files_list = os.listdir(file_dir)
    # for i in files_list:
        # if i.endswith('.jpg') or i.endswith('.JPG'):
            # filename = get_filepath_shotname_extension(i)
            # img = Image.open(i)
            # img_out = img.resize((150,150),Image.ANTIALIAS)
            # img.save("module_"+filename[0]+'.png','PNG')
            # print(i)
    # for root, dirs, files in os.walk(file_dir):
    #     count = 1
        # for i in files:
    #         if i.endswith('.jpg') or i.endswith('.png'):
    #             filename = get_filepath_shotname_extension(i)
    #             # img = Image.open(i)
    #             # img_out = img.resize((150,150),Image.ANTIALIAS)
    #             # img_out.save(filename[0]+'.png','PNG')
    #             # count+=1
                # print(filename[0])
                # print(i)

def rename_file(path):
    files_list = os.listdir(path)
    for file in files_list:
        """
        所有文件夹批量重命名为大写
        """
        old_path = os.path.join(path, file)
        if os.path.isfile(old_path):
            filename = get_filepath_shotname_extension(old_path)[0]
            filetype = get_filepath_shotname_extension(old_path)[1]
            """ 批量更改图片格式为png """
            if filetype == ".jpg":
                img = Image.open(old_path)
                img.save(filename+'.png', 'PNG')
                print(old_path)
            # pass
        else:
            rename_file(old_path)
            # os.rename(file, file.upper())
            # print(file)
        # os.rename(file, file.upper())
        # print(file)
        """
        遍历所有文件，并重命名
        """
        # old_path = os.path.join(path, file)
        # if os.path.isfile(old_path):
        #     # print("file: %s"%old_path)
        #     filename = get_filepath_shotname_extension(old_path)[0]
        #     filetype = get_filepath_shotname_extension(old_path)[1]
        #     if filetype == ".m5f":
        #         print(filename)
        #         new_path = os.path.join(path, "\\example_unit_"+filename+filetype)
        #         os.rename(old_path, new_path)
        # else:
        #     rename_file(old_path)


        # i=i+1
        # Olddir=os.path.join(path,file);#原来的文件路径
        # print(Olddir)
        # if os.path.isdir(Olddir):#如果是文件夹则跳过
        #         continue;
        # filename=os.path.splitext(file)[0];#文件名
        # filetype=os.path.splitext(file)[1];#文件扩展名
        # Newdir=os.path.join(path,"example_unit_"+filename+filetype);#新的文件路径
        # os.rename(Olddir,Newdir)#重命名
        """
        移动文件到指定文件夹
        """
        # print(file)
        # filepath = cur_path+"\\"+file
        # if os.path.isdir(filepath):
        #     print(filepath)
        #     os.chdir(filepath)
        #     rename_file(filepath)
        # elif os.path.isfile(filepath):
        #     # filename = get_filepath_shotname_extension(file)
        #     # img = Image.open(i)
        #     # img.save(filename[0]+'.png', 'PNG')
        #     print(file)
        #     # pass

if __name__ == "__main__":
    rename_file(cur_path)
