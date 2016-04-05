#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import exifread

def filter_untagged(directory):
    for file in os.listdir(directory):
        if file.endswith('.jpg'):
            file_path = os.path.join(directory, file)
            
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f)
                has_latitude = 'GPS GPSLatitude' in tags.keys()
                has_longitude = 'GPS GPSLatitude' in tags.keys()

                if not has_latitude and not has_longitude:
                    print ("[DELETE] %s" % file_path)
                    os.remove(file_path)


def show_usage():
    print("Usage: ./filter_untagged.py directory")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        show_usage()
    else:
        directory = sys.argv[1]
        if not os.path.isdir(directory):
            show_usage()
        else:
            filter_untagged(directory)
