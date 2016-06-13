import sys

def sed(pattern,replacement,source,dest):
    """
    Read the first file and write contents into second file.
    If the pattern string appears anywhere in the in the file, it should be replaced with the replacement string.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    try:
        fin = open(source)
        fout = open(dest,'w')
        for line in f1:
            line = line.replace(pattern, replace)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print "Something went wrong"

def main(name):
    pattern = 'pattern'
    replace = 'replacendum'
    source = name
    dest = name + ".replaced"
    sed(pattern, replace, source, dest)

if __name__ == '__main__':
    main(*sys.argv)
