#!/usr/bin/env python3
import requests, dsstore, sys

def processfolder(site ,foldername, log):
    r=requests.get(f"{site}/{foldername}.DS_Store")
    if r.content:
        try:
            d=dsstore.DS_Store(r.content,debug=False)
            files=d.traverse_root()
            for i in files:
                if i=='.':
                    continue
                log.write(f"{site}/{foldername+i}\n")
                if '.' in i:
                    continue
                processfolder(site,foldername+i+"/",log)
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: dsscanner.py <URL> <LOGFILE>")
    with open(sys.argv[2],"w") as log:
        processfolder(sys.argv[1], '', log)