#!/bin/bash

# for building
mydir=$(dirname $BASH_SOURCE)
export SPACK_ROOT=$mydir/spack
source $SPACK_ROOT/share/spack/setup-env.sh

# for runtime
spack load -r gcc
spack load -r bempp

