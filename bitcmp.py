#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Compare files bit by bit')
parser.add_argument('file1', metavar='file1', type=argparse.FileType('rb'), help='first file')
parser.add_argument('file2', metavar='file2', type=argparse.FileType('rb'), help='second file')
parser.add_argument('byteCount', metavar='count', type=int, nargs='?', help='number of bytes to compare')
args = parser.parse_args()

def bitCmp(f1, f2, num):
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    for i in range(num):
        str1 += bin(f1[i])[2:].zfill(8)
        str2 += bin(f2[i])[2:].zfill(8)
        for j in range(i * 8, i * 8 + 8):
            if str1[j] == str2[j]:
                str3 += '='
            else:
                str3 += '!'
        str4 += "76543210"
    print(str1)
    print(str2)
    print(str3)
    print(str4)

if __name__ == '__main__':
    f1 = args.file1.read()
    f2 = args.file2.read()
    if (args.byteCount):
        n = min(args.byteCount, len(f1), len(f2))
    else:
        n = min(len(f1), len(f2))
    bitCmp(f1, f2, n)


