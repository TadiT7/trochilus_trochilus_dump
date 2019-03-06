import json
import sys


def main():

    data = json.load(open('/sdcard/Download/FAP/TestResult.txt'))

    if sys.argv[1]=='all':
        print(data)
    else:
        result=data[sys.argv[1]][sys.argv[2]][sys.argv[3]][sys.argv[4]]
        print(result)

if __name__ == '__main__':
    main()
