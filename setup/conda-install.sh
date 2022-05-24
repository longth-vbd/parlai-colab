#!/bin/bash

ROOT=$PWD

# install conda
mkdir .tmp
cd .tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -p $ROOT/miniconda3

echo "Done!"