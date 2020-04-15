import os
import fnmatch
import shutil

ini_path = os.getcwd()
in_f= ini_path + '\\Input\\list.txt'
# Output folder to store the files founded
out_f= ini_path + '\\Output'

# Root Path to start searching
search_path= input("Please write or paste the Path where you want to start the Search.\n")
os.chdir(search_path)
cur_path= os.getcwd()


def create_list(input_file_path):
    print("**************************************************************")
    print("-----BEGIN-----")
    with open(input_file_path, 'r') as file:
        pattern_list = file.read().splitlines()
        file.close()
    print("-----Pattern List: ",pattern_list," -----")
    print("------END------")
    return pattern_list


def return_file(pattern):
    file_ret=[]
    print("**************************************************************")
    print("-----BEGIN Search fiels-----")
    for p in pattern:
        print("-----Pattern: ",p)
        for dirpath, _, files in os.walk(cur_path):
            for file in files:
                if fnmatch.fnmatch(file.upper(), p.upper()):
                    stra = os.path.join(dirpath, file)
                    file_ret.append(stra)
                    print("-----File Found: ",file)
                    print("")
    print("------END------")
    return file_ret
        
def copy_file(file,out_path):
    print("**************************************************************")
    print("-----BEGIN Copy of files-----")
    for f in file:
        shutil.copy(f, out_path)
        print("Copy of file: ", f)


copy_file(return_file(create_list(in_f)), out_f)
print("**************************************************************")
