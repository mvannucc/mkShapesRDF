#!/bin/bash 


env=$(hostname)
substring="lxplus"

if [[ $env == *$substring* ]]; then
    echo "Installing on $substring."

    sourceCommand="source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh"

    eval "$sourceCommand"
    python -m venv --system-site-packages myenv
    source myenv/bin/activate

    python -m pip install -e .

    python -m pip install --no-binary=correctionlib correctionlib

    
    cat <<EOF > start.sh
#!/bin/bash
$sourceCommand
source `pwd`/myenv/bin/activate
EOF


    chmod +x start.sh

    wget https://gpizzati.web.cern.ch/mkShapesRDF/jsonpog-integration.tar.gz
    tar -xzvf jsonpog-integration.tar.gz
    rm -r jsonpog-integration.tar.gz
    mv jsonpog-integration mkShapesRDF/processor/data/



else

    echo "installing on $env"

    which python

    which python3

    python3 -m venv --system-site-packages myenv
    source myenv/bin/activate

    pip --version

    python -m pip install --upgrade pip

    echo "new pip version is"

    pip --version

    python -m pip install -e .[docs,dev]

    python -m pip install --no-binary=correctionlib correctionlib


    wget https://gpizzati.web.cern.ch/mkShapesRDF/jsonpog-integration.tar.gz
    tar -xzvf jsonpog-integration.tar.gz
    rm -r jsonpog-integration.tar.gz
    mv jsonpog-integration mkShapesRDF/processor/data/


    cat <<EOF > start.sh

#!/bin/bash                                                                                                                                      
source `pwd`/myenv/bin/activate                                                                                                                  
export STARTPATH=`pwd`/start.sh                                                                                                                  
source `pwd`/fix_xrdfs.sh
EOF

    chmod +x start.sh


fi
