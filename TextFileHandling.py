import glob
import  os
from QuickHash import md5
from tika import parser


text_metadata =[]


def tika_parser(filepath):
    # Parse data from file
    file_data = parser.from_file(filepath)
    # Get files text content
    text = file_data['content']
    return text


def extract_metadata(filename):
    # extract metadata
    global parse_value, text_file_size, hash_value,date_of_creation
    parse_value = tika_parser(filename)
    text_file_size =os.path.getsize(filename)
    hash_value = md5(filename)
    date_of_creation = os.path.getctime(filename)


# Loop through all jpeg files and create a list for metadatda extraction for each
def loop_text(filepath):
    for text_file in glob.glob(os.path.join(filepath,"*.docx")):
        parse_value = tika_parser(text_file)
        null_value = extract_metadata(text_file)
        # convert output into a list
        text_metadata.append((text_file,date_of_creation,hash_value, parse_value, text_file_size))