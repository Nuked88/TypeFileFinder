import csv,os
from ast import literal_eval

#get args from command line
def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='Find file type in a binary file')
    parser.add_argument('-f', '--file', help='File to open', required=True)
    parser.add_argument('-o', '--offset', help='Offset to reach (es. of you input -o 0x1d85 it will search headers until it reach that offset', required=False ,default="0")
    parser.add_argument('-l', '--length', help='Length of header minimum (It will exclude header more greater of that) Default: 3', required=False, default=3)
    args = parser.parse_args()
    return args

#search record in a csv file
def string_to_hex(string):
    string = "\\x"+string.replace(" ", "\\x")
    return string 

def csv2dict(filename):
    didi = {}
    file = open(filename, "r")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        didi[string_to_hex(row[1])] = f"{row[2]} - {row[0]}"

    return didi

def file_type(filename,maxoffset="0",minlen=3):
    type_dict = csv2dict("file_sigs_RAW.txt")
    type_found = []
    with open(filename, 'rb') as f:
        try:
            file_start = f.read()
        except Exception as e:
            file_start = ""
            print(("skip"))
            pass
    
    for magic,filetype  in type_dict.items():
        try:
            magic_byte = magic.encode().decode('unicode_escape').encode("raw_unicode_escape")
            if len(magic_byte) >= minlen:

                if file_start.find(magic_byte)!=-1:
                    offset = file_start.find(magic_byte)
                    
                    if offset<=literal_eval(maxoffset) or maxoffset=="0":
                        print(f"Offset: {hex(offset)}")
                        print(f"Head: {magic_byte}")
                        print(f"Filetype: {filetype}")
                        print("\n")
                    type_found.append(filetype)
        except Exception as e:
            pass


file_type(filename=get_args().file,maxoffset=get_args().offset,minlen=get_args().length)
