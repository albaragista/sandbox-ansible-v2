import re
import sys
import time

def getFile():
    try:
        # print(JOB_NAME)
        # print(FILE_LOCATION)

        JOB_NAME = sys.argv[1]
        FILE_LOCATION = sys.argv[2]
        pattern= "job_name.*"+JOB_NAME
        # print(pattern)
        found= False
        with open(FILE_LOCATION, 'r') as searchfile:
            for line in searchfile:
                match= re.search(pattern, line, re.M|re.I)
                if match != None :
                    found= True
                    break
                else:
                    found= False
                    # print("NOT")
        return found
    except Exception as er:
        print("ERROR")

def run():
    getStatus= getFile()
    print(getStatus)

if __name__ == '__main__':
    run()
