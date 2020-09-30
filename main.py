import os
from ClassificationOfFile import create_dirs, arrange
from ImageHandling import img_metadata, loop_jpg
from ImgDatabase import bullk_insert_img_file
from TextFileHandling import  text_metadata,loop_text
from TextDatabase import  bullk_insert_text_file

class Main:
    create_dirs()
    arrange()
    current_dir = (os.getcwd())
    loop_jpg(os.path.join(current_dir + "\jpg_files"))
    bullk_insert_img_file(img_metadata)
    os.chdir(current_dir)
    loop_text(os.path.join(current_dir+"\docx_files"))
    bullk_insert_text_file(text_metadata)
    print("End")
