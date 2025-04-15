Technical Review
################

This section includes instructions to reproduce the results of the analysis.


Install software 
++++++++++++++++

Simulation 
++++++++++

Reconstruction
++++++++++++++

Process data to Level 5 
+++++++++++++++++++++++

The following instructions to install the software are for the IceCube cluster and extracted from the intructions of the `dnn_reco <https://user-web.icecube.wisc.edu/~mhuennefeld/docs/dnn_reco/html/pages/installation.html>`_ framework.

.. code-block:: bash 

    # load cvmfs python environment
    eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

    mkdir /data/user/{USER}/technical_review/virtual_envs

    cd /data/user/{USER}/technical_review/virtual_envs

    python -m virtualenv py3-v4.3.0_tensorflow2.14

    source py3-v4.3.0_tensorflow2.14/bin/activate

    # change activation script such that it prepends the path
    # to the virtual environment to the PYTHONPATH environment variable
    perl -i -0pe 's/_OLD_VIRTUAL_PATH\="\$PATH"\nPATH\="\$VIRTUAL_ENV\/bin:\$PATH"\nexport PATH/_OLD_VIRTUAL_PATH\="\$PATH"\nPATH\="\$VIRTUAL_ENV\/bin:\$PATH"\nexport PATH\n\n# prepend virtual env path to PYTHONPATH if set\nif ! \[ -z "\$\{PYTHONPATH+_\}" \] ; then\n    _OLD_VIRTUAL_PYTHONPATH\="\$PYTHONPATH"\n    export PYTHONPATH\=\$VIRTUAL_ENV\/lib\/python3.7\/site-packages:\$PYTHONPATH\nfi/' py3-v4.3.0_tensorflow2.14/bin/activate

    perl -i -0pe 's/        export PYTHONHOME\n        unset _OLD_VIRTUAL_PYTHONHOME\n    fi/        export PYTHONHOME\n        unset _OLD_VIRTUAL_PYTHONHOME\n    fi\n\n    if ! \[ -z "\$\{_OLD_VIRTUAL_PYTHONPATH+_\}" \] ; then\n        PYTHONPATH\="\$_OLD_VIRTUAL_PYTHONPATH"\n        export PYTHONPATH\n        unset _OLD_VIRTUAL_PYTHONPATH\n    fi/' py3-v4.3.0_tensorflow2.14/bin/activate

    pip install tensorflow==2.14 tensorflow_probability==0.22.1

    cat << 'EOF' >> py3-v4.3.0_tensorflow2.14/bin/activate
    export CUDA_HOME=/data/user/mhuennefeld/software/cuda/cuda-11.8
    export PATH=$PATH:${CUDA_HOME}/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CUDA_HOME}/lib64
    EOF

    pip install pybind11

    export I3_BUILD=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/metaprojects/icetray/v1.12.0/

    export I3_SRC=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/metaprojects/icetray/v1.12.0/

    pip install git+ssh://git@github.com/icecube/TFScripts

    pip install git+ssh://git@github.com/icecube/ic3-labels

    pip install git+ssh://git@github.com/icecube/ic3-data

    ########################################################################
    # typically,
    # if there is a HDF5 version mismatch we must install h5py from source
    # Use: 'h5cc -showconfig' to obtain hdf5 configuration and library version
    # use: 'ls -lah $(which h5cc)' to obtain path to hdf5 directory
    pip uninstall h5py

    HDF5_VERSION=1.14.0 HDF5_DIR=/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/spack/opt/spack/linux-centos7-x86_64_v2/gcc-13.1.0/hdf5-1.14.0-4p2djysy6f7vful3egmycsguijjddkah pip install --no-binary=h5py h5py==3.11.0
    ########################################################################

    mkdir /data/user/{USER}/technical_review/repositories 

    cd /data/user/{USER}/technical_review/repositories

    git clone https://github.com/mhuen/dnn_reco.git

    # install package
    pip install -e dnn_reco

    git clone https://github.com/mhuen/ic3-processing.git

    pip install -e ic3-processing

    # Now you can verify your installation. Log out from cobalt and log in again.
    # load icecube environment
    eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

    /cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/RHEL_7_x86_64/metaprojects/icetray/v1.12.0/env-shell.sh

    source /data/user/{USER}/technical_review/virtual_envs/py3-v4.3.0_tensorflow2.14/bin/activate

    echo $CUDA_HOME
    # this should print: /data/user/mhuennefeld/software/cuda/cuda-11.8

    python -c 'import tensorflow as tf; print(tf.__version__)'
    # this should print some information about about tensorflow, which can take up to a minute, the the last print should be: 2.14.0

    python -c 'import dnn_reco; import tfscripts; import ic3_labels; import ic3_data'
    # this should not print any error messages (Could not find TensorRT -- is expected)

    # install analysis repo
    cd /data/user/{USER}/technical_review/repositories

    git clone git@github.com:icecube/dnn_selections.git

    pip install -e dnn_selections

    cd dnn_selections

    git checkout -b AnalysisPipeline origin/AnalysisPipeline

.. note::
    The prebuilt tensorflow binary is built to use avx2 and ssse3 instructions among others.
    These are not available on cobalts 1 through 4.
    Attempting to import tensorflow will lead to an "illegal instructions"
    error. Therefore, if running on the cobalts, simply choose one of the
    newer machines: cobalt >=5.
    On NPX, if running CPU jobs, you can request nodes with avx2 and ssse3
    support by adding: ``requirements = (TARGET.has_avx2) && (TARGET.has_ssse3)``. This is only necessary for CPU jobs. For GPU jobs,
    these requirements should not be set.

Unfolding
+++++++++

