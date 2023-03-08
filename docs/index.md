# Welcome to mkShapesRDF

## Installation 

Git clone the project and work with the `v0.0.1` 

``` bash

git clone https://github.com/giorgiopizz/mkShapesRDF.git
git checkout v0.0.1

```

Lxplus is currently the only supported machine.
In order to install the package it's first necessary to source the right LCG release:
``` bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_102/x86_64-centos7-gcc11-opt/setup.sh
```
now the right python version (3.9) and it's bindings with ROOT are setup.
It's highly reccomended to create a virtual environment for the installation:
``` bash
python -m venv --system-site-packages myenv
```
and of course activate it:
``` bash
source myenv/bin/activate
```

Now you can proceed to the simple installation:
```
pip install -e .
```

From now on, when you will login again on lxplus you will just have to run the setup command:
```
. ./start.sh
```

## Configure the configuration folder (e.g. `examples/2016Real`):
Documentation on the configuration folder structure at [this page](config.md)
<!-- - configuration.py 

- aliases.py
- configuration.py
- cuts.py
- nuisances.py
- plot.py
- samples.py
- variables.py -->

## Run the analysis:
``` bash
mkShapesRDF -o 0 -f . -b 1
```
`-o` indicates the operationMode:
- 0 run analysis
- 1 check batch output and errs
- 2 merge root files
- 3 plot them

For the provided example (2016Real) it's estimated an execution time of ~ 10 mins running on lxbatch (condor on lxplus) @ CERN when disabling nuisances.


It's highly recommended to limit input ROOT files at the first run to check for errors. The following command will only take 1 event for each sample type:
``` bash
python mkShapesRDF.py -o 0 -f . -l 1
```

## Check for errors
After all the jobs finished (or most of them did) you can run `mkShapesRDF.py -o 1 -f .` to know which jobs failed and why

## Merge files
If all the jobs succeeded run the merger with the option: 
```bash
python mkShapesRDF.py -o 2 -f .
```

## Plots
Plot with 
```bash
python mkShapesRDF.py -o 3 -f .
```
which will create the plots to the specified paths provided in `configuration.py` 