# Simulation Tutorials

Provides sample cases and reinterpretation of classical tutorials

## OpenFOAM

OpenFOAM tutorials from basic to (very) advanced.

Recommended operating systems:

- OpenSUSE (as recommended by OpenFOAM.com)
- Ubuntu (most users are on this platform)
- Centos (quite outdated for using other tools)
- WSL (bad user experience on the long term)

## SU2

### Build

Here we build [SU2](https://github.com/su2code/SU2) with [Mutation++](https://github.com/mutationpp/Mutationpp) support. Before starting we install external dependencies with:

```bash
sudo apt install -y cmake mpich swig libopenblas-dev liblapacke-dev
pip install --user mpi4py
```

Next we clone SU2 with `git clone https://github.com/su2code/SU2.git` and `cd SU2/` to start the configuration and compilation. To optimize for the local architecture you need to export a variable as follows. The options below are discussed more in detail [here](https://stackoverflow.com/questions/56870475).

```bash
export CXXFLAGS='-march=native -mtune=native -funroll-loops'
```

You might want to define a location for your external packages. A common solution is `export PACKAGES="${HOME}/Packages"`. With this path defined declare the following and add it to your `.bashrc` file.

```
export PACKAGES="${HOME}/Packages"

export SU2_HOME="${PACKAGES}/SU2"
export SU2_RUN="${SU2_HOME}/bin"
export PATH="${SU2_RUN}:${PATH}"
export PYTHONPATH=${SU2_RUN}:${PYTHONPATH}
export LD_LIBRARY_PATH="${SU2_HOME}/lib:${LD_LIBRARY_PATH}"
```

During the build I found an issue with `Ninja` executable. An workaround to get compilation working was:

```
export PATH=$(pwd):$PATH
export Ninja=$(pwd)/ninja
rm -rf externals/codi/ externals/medi/
```

Finally, SU2 configuration is done with:

```
./meson.py build \
    -Dwith-mpi=enabled \
    -Dwith-omp=true \
    -Denable-tecio=true \
    -Denable-cgns=true \
    -Denable-autodiff=true \
    -Denable-directdiff=true \
    -Denable-pywrapper=true \
    -Denable-mkl=false \
    -Dmkl_root=/opt/intel/mkl \
    -Denable-openblas=true \
    -Dblas-name=openblas \
    -Denable-pastix=false \
    -Dpastix_root=externals/pastix/ \
    -Dscotch_root=externals/scotch/ \
    -Dcustom-mpi=false \
    -Denable-tests=true \
    -Denable-mixedprec=true \
    -Dextra-deps=lapack \
    -Denable-mpp=true \
    -Dopdi-backend=auto \
    -Dcodi-tape=JacobianLinear \
    -Dopdi-shared-read-opt=true \
    -Dlibrom_root='' \
    -Denable-librom=false \
    --prefix=${SU2_HOME} \
    --optimization=2
```

Compilation, install and testing is done with the following:

```
./ninja -C build install
./ninja -C build test
```
