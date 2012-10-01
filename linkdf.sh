#!/bin/bash

# that's 'linkdf' as in 'link .files'

# This file links file from this directory to a users home directory
# mostly for quick installation of dotfiles
# the EXCLUDE variable contains a list of files and directories
# that should not be linked

EXCLUDE=".git bak sen .gitignore"
# the git folder, bak'd up files, sensitive files, .gitignore

_BACKUP=1
FILES=`find . -mindepth 1 -maxdepth 1 -print | cut -d'/' -f2-`

while [ $# -gt 0 ]; do
    case "$1" in 
        -n|--no-backup)
            _BACKUP=0
            ;;
    esac
    shift
done

is_excluded () {
    for item in $EXCLUDE; do
        if [ $item == $1 ]; then
            return 0
        fi
    done
    return 1
}

for file in $FILES; do
    if is_excluded $file; then
        echo $file is excluded
        continue
    fi
    if [ -e $HOME/$file -a $_BACKUP -eq 1 ]; then
        if [ ! -d "bak" ]; then
            mkdir "bak"
        fi
        mv $HOME/$file "bak"
        echo backing up $HOME/$file
    else if [ -e $HOME/$file -o -L $HOME/$file -a $_BACKUP -eq 0 ]; then
        echo Removing $HOME/$file
        rm -rf $HOME/$file
        fi
    fi
    ln -s "`pwd`/$file" $HOME
    echo linking $file
done
