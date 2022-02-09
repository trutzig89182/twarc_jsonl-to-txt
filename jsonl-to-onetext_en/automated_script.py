import os
from jsonl_to_onetxt_en import writetweetstotxt


main_directory = os.getcwd()


for entry in os.scandir(main_directory):
    # check if entry in main directory (the script is in) is a folder
    if os.path.isdir(entry):
        print(entry.path)
        writetweetstotxt(os.path.realpath(entry), entry.name)
