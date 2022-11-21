import sys
import fileinput
import os

# sys.stdout.write(str(datetime.datetime.now().strftime("%H:%M:%S"))+'\t')

# # file_object = open(r'C:\Users\DUMA1KOR\Desktop\Codes\React\Master-TARA-Creator-main\flask\FilePath.txt')
# line = sys.stdin.readlines()
# print(line)

# if 'File'
# for line in sys.stdin:
#     sys.stdout.write(str(datetime.datetime.now().strftime("%H:%M:%S"))+'\t')
#     sys.stdout.write(line)
#     sys.stdout.flush()
#     # time.sleep(1)

lines = []


def sendFileData():
    with fileinput.input(files=r'C:\Users\DUMA1KOR\Desktop\Codes\React\Master-TARA-Creator-main\flask\FilePath.txt') as f:
        for line in f:
            global lines
            lines = line
    return lines

