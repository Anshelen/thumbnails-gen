#!/usr/bin/env python

try:
    from resizeimage import resizeimage
except ImportError:
    print('Error, Module python-resize-image is required. '
          'Run "pip install python-resize-image".')
    import sys
    sys.exit(1)

from PIL import Image
from os import listdir
from os.path import isfile, join, exists
import argparse


def get_target_file_path(filename, fmt):
    filename = join(to, filename)
    dot_index = filename.rfind('.')
    name, ext = filename[:dot_index], filename[dot_index + 1:]
    return name + '_' + fmt + '.' + ext


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to originals folder',
                        type=str)
    parser.add_argument('--output', '-o', help='Path to thumbnails folder',
                        type=str)
    parser.add_argument('--formats', '-f', nargs='+',
                        help='Formats like 200w or 600h', type=str)
    args = parser.parse_args()
    path, to, formats = args.input, args.output, args.formats

    if not path:
        path = input('Enter path to originals: ')
    if not to:
        to = input('Enter path to thumbnails folder: ')
    if not formats:
        formats = input('Enter target formats (like 200w or 600h) '
                        'separated by space: ').split()

    print('Input:', path, to, formats, sep='\n')

    created, skipped, errors = 0, 0, 0
    for fmt in formats:
        for file_name in listdir(path):
            file_path = join(path, file_name)
            if isfile(file_path):
                target_file_path = get_target_file_path(file_name, fmt)
                if not exists(target_file_path):
                    try:
                        fd = open(file_path, 'rb')
                        img = Image.open(fd)
                        if fmt[-1] == 'h':
                            img = resizeimage.resize_height(img, int(fmt[:-1]))
                        elif fmt[-1] == 'w':
                            img = resizeimage.resize_width(img, int(fmt[:-1]))
                        else:
                            raise ValueError('Not supported format')
                        img.save(target_file_path, img.format)
                        fd.close()
                        created += 1
                        print('Created', target_file_path)
                    except Exception as e:
                        errors += 1
                        print('Exception: ', e)
                else:
                    skipped += 1
                    print('Skipped', target_file_path)

    print(f'Finished. Created: {created} Skipped: {skipped}, Errors: {errors}')
