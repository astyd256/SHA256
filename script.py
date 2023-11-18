import sys
import hashlib

if 1 < len(sys.argv) < 4:
    path = sys.argv[1]
    with open(path, 'rb') as file:
        contents = file.read()
    file_digest = hashlib.sha256(contents).hexdigest()
    print(f"File digest: {file_digest}")
    if len(sys.argv) == 3:
        print(f"is file digest equeal to your digest? {sys.argv[2] == file_digest}")
else:
    print("Wrong number of arguments. Usage: python script.py [path_to_file] or python script.py [path_to_file] [SHA256]")
    exit(1)    
    