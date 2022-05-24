#!/bin/sh

ROOT=$PWD
source $ROOT/miniconda3/bin/activate
conda create -n parl-py38-conda-env python=3.8

echo "Created conda environment: parl-py38-conda-env"