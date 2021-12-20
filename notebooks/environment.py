import os

# https://bugs.openfoam.org/view.php?id=3163
os.environ["OMPI_MCA_btl_vader_single_copy_mechanism"] = "none"

os.environ["WM_PROJECT"] = "OpenFOAM"
os.environ["WM_PROJECT_USER_DIR"] = "/home/walter/OpenFOAM/walter-v2106"

os.environ["FOAM_MPI"] = "sys-openmpi"
os.environ["FOAM_API"] = "2106"

os.environ["FOAM_APP"] = "/usr/lib/openfoam/openfoam2106/applications"
os.environ["FOAM_ETC"] = "/usr/lib/openfoam/openfoam2106/etc"
os.environ["FOAM_SRC"] = "/usr/lib/openfoam/openfoam2106/src"
os.environ["FOAM_SOLVERS"] = "/usr/lib/openfoam/openfoam2106/applications/solvers"
os.environ["FOAM_TUTORIALS"] = "/usr/lib/openfoam/openfoam2106/tutorials"
os.environ["FOAM_UTILITIES"] = "/usr/lib/openfoam/openfoam2106/applications/utilities"

os.environ["FOAM_APPBIN"] = "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/bin"
os.environ["FOAM_LIBBIN"] = "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib"
os.environ["FOAM_SITE_APPBIN"] = "/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/bin"
os.environ["FOAM_SITE_LIBBIN"] = "/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/lib"
os.environ["FOAM_USER_APPBIN"] = "/home/walter/OpenFOAM/walter-v2106/platforms/linux64GccDPInt32Opt/bin"
os.environ["FOAM_USER_LIBBIN"] = "/home/walter/OpenFOAM/walter-v2106/platforms/linux64GccDPInt32Opt/lib"

os.environ["FOAM_RUN"] = "/home/walter/OpenFOAM/walter-v2106/run"
os.environ["LD_LIBRARY_PATH"] = ":".join([
    "/home/walter/OpenFOAM/walter-v2106/platforms/linux64GccDPInt32Opt/lib",
    "/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/lib",
    "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib",
    "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib/dummy",
    "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib/sys-openmpi",
    "/usr/lib/x86_64-linux-gnu/openmpi/lib",
    "/opt/SU2/lib"
])

os.environ["PATH"] = ":".join([
    "/home/walter/OpenFOAM/walter-v2106/platforms/linux64GccDPInt32Opt/bin",
    "/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/bin",
    "/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/bin",
    "/usr/lib/openfoam/openfoam2106/bin",
    "/usr/lib/openfoam/openfoam2106/wmake",
    "/opt/SU2/bin",
    "~/.local/bin",
    "/home/walter/.cargo/bin",
    "/usr/local/nvidia/bin",
    "/usr/local/cuda/bin",
    "/usr/local/sbin",
    "/usr/local/bin",
    "/usr/sbin",
    "/usr/bin",
    "/sbin:/bin"
])

os.environ["SU2_HOME"] = "/opt/SU2"
os.environ["SU2_RUN"] = "/opt/SU2/bin"
os.environ["PYTHONPATH"] = "/opt/SU2/bin"
