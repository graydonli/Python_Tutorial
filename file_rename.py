# from PIL import Image
import os

def get_filepath_shotname_extension(filename):
    (filepath, tempfilename) = os.path.split(filename)
    (shotname, extension) = os.path.splitext(tempfilename)
    # print("filepath: %s, shotname: %s, extension: %s"%(filepath, shotname, extension))
    return (shotname, extension)

def image_resize(file_dir):
    for root, dirs, files in os.walk(file_dir):
        count = 1
        for i in files:
            filename = get_filepath_shotname_extension(i)
            # unit_name = filename[0].split("module_")
            unit_name = filename[0].split("module_")
            if unit_name[0] == '':
                # print(unit_name)
            # if "M5GO_Unit_" in filename[0]:
                # unit_name = filename[0].split("unit_")
            #     print(unit_name)
                # print(os.path.join(root, unit_name[1]))
                a = os.rename(os.path.join(root, i), os.path.join(root, unit_name[1]+'.md'))
                print(a)
            # img = Image.open(i)
            # # img_out = img.resize((150,150),Image.ANTIALIAS)
            # img.save(filename[0]+'.png','PNG')
            # print(filename[0])

if __name__ == "__main__":
    image_resize(".")