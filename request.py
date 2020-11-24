#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t','--target',help="objetivo")
parser = parser.parse_args()


def main():
    if parser.target:
            url = requests.get(url=parser.target)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
    else:
        print("no hay objetivo")
        
if __name__ == '__main__':
    main()
