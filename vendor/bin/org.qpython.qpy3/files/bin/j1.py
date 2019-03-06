import json
import sys


def main():
    if sys.argv[1]=='reset':
        filew = open("/data/FAP/log/AOP_log.txt", "w+")
        filew.write('[]')
        filew.close()
    else:
        filer = open("/data/FAP/log/AOP_log.txt", "r+")
        fileaString = filer.read()
        data_s=filer.tell()
        filer.close()
        if sys.argv[1]=='data':
            data='{"'+sys.argv[2]+'":"'+sys.argv[3]+'"}'
        if sys.argv[1]=='val':
            data='{"'+sys.argv[2]+'":['+sys.argv[3]+']}'
        if 1:
            filew = open("/data/FAP/log/AOP_log.txt", "w+")
            filew.write(fileaString)
            filew.seek(data_s-1)
            if data_s!=2:
                filew.write(',')
            filew.write(data)
            filew.write(']')
            filew.close()
    
    
if __name__ == '__main__':
    main()
