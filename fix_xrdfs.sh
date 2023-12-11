#!/bin/bash

export LD_LIBRARY_PATH=$(root-config --libdir):$(pwd)/xrdfs_locallib/lib:/.singularity.d/libs
