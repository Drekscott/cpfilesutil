#! usr/bin/python

"""
Author: Dreyton Scott
11/7/16

Program Purpose: To copy given files from command line to
a destination directory using os and sys modules.
Program should be invoked as:

./a8.py <filepath> <filepath2> ... <dest-dir>

"""

import os, sys

def cp1file(file, dest):
    """
    parameters: file(file to copy), dest(path of destination),
    copies the given source-file-path to destination-file-path
    returns 0 on success.

    """
    
    with open(file, 'r') as infile:
        with open(dest,'w') as outfile:
            for line in infile:
                outfile.write(line)
            outfile.close()
        infile.close()
    return 0

def cpfiles():
    """
    copies the files to dest-dir. For each source-file
    that is a regular file and can be copied, supplies error messages, builds
    the destination file path and copy it to destination, uses cp1file() to make
    the actual copy. Once all files have been made prints the count of files copied
    successfully.
    """
    file_count = 0
    for arg in sys.argv:
        dst_path = os.path.join(os.path.dirname(sys.argv[len(sys.argv)-1]),os.path.basename(arg))
        if (arg != sys.argv[0]) and (arg != sys.argv[len(sys.argv)-1]):
            if not (os.path.isfile(arg)):
                print ("%s : no such file or dir\n" % arg)
            elif (os.path.isfile(dst_path)):
                print ("%s : not copied, exists at destination\n" % arg)
            else:
                cp1file(arg, dst_path)
                file_count+=1
    print ("%d files copied successfully\n" % file_count)
    return 0

def checkargs():
    """
    checks for proper number of args and nature of
    the last arg passed to main(); called by main(), returns 0 on success
    sys.exit(1) otherwise. Prints meaningful error messages.
    """
    
    last_arg = len(sys.argv)-1
    if (len(sys.argv)<3):
        print("usage: %s <file-path1> <file-path2> ... <dest>\n" % sys.argv[0])
        sys.exit(1)
    if not (os.path.isdir(sys.argv[last_arg])):
        print("Destination provided does not exists or is not a directory\n")
        sys.exit(1)
    return 0

def main():
    """
    makes calls to checkargs() and cpfiles(). exits with 0 status
    """
    checkargs()
    cpfiles()
    sys.exit(0)
if __name__ == "__main__":
    main()
