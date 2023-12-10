"""Build a nv_updater plugin.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_updater project. 

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/nv_updater
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib-Alpha/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}nv_updater.py'
TARGET_FILE = f'{BUILD}nv_updater.py'

os.makedirs(BUILD, exist_ok=True)


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvupdaterlib', '../../novelyst_updater/src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'noveltreelib', '../../noveltree/src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'novxlib', '../../novxlib-Alpha/src/')
    print('Done.')


if __name__ == '__main__':
    main()
