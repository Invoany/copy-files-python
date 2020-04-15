import os
import fnmatch
import shutil

ini_path = os.getcwd()
in_f=r'C:/Users/jorge/OneDrive - Portugal Telecom/Jorge Nunes/Python/Return_Files/Input/lista.txt'

# Output folder to store the files founded
out_f=r'C:/Users/jorge/OneDrive - Portugal Telecom/Jorge Nunes/Python/Return_Files/Output'

# Root Path to start searching
os.chdir(r'C:\Users\jorge\Downloads')
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
        for dirpath, dirnames, files in os.walk(cur_path):
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
