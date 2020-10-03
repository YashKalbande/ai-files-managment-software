import os
import glob
from PIL import Image, ExifTags
from QuickHash import md5

img_metadata =[]


def extract_metadata(filename):
    # extract metadata
    image = Image.open(filename)
    exif = {ExifTags.TAGS[k]: v for k, v in image.getexif().items() if k in ExifTags.TAGS}
    global model, date_time, image_size, hash_value
    model = exif['Model']
    date_time =exif['DateTimeDigitized']
    image_size = os.path.getsize(filename)
    hash_value = md5(filename)


# Loop through all jpeg files and create a list for metadata extraction for each
def loop_jpg(filepath):
    for image_name in glob.glob(os.path.join(filepath,"*.jpg")):
        md_file = extract_metadata(image_name)
        # convert output into a list
        img_metadata.append((image_name , hash_value, model, date_time, image_size))

