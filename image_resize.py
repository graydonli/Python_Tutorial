from PIL import Image
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
            if i.endswith('.jpg') or i.endswith('.JPG'):
                filename = get_filepath_shotname_extension(i)
                img = Image.open(i)
                # img_out = img.resize((150,150),Image.ANTIALIAS)
                img.save(filename[0]+'.png','PNG')
                count+=1
                print(filename[0])

if __name__ == "__main__":
    image_resize(".")
