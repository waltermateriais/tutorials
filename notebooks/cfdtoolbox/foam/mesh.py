# -*- coding -*-
import pyvista as pv

def plot_mesh(mesh_file, cpos=None, mtm=None, notebook=True):
    """ Display the mesh with axes and camera/zoom configuration.
    
    Parameters
    ----------
    mesh_file : path-like
        Path to mesh file to be parsed for display.
    cpos : list(tuple(floats))
        Camera position passed to `Plotter.show`.
    mtm : np.ndarray [4x4]
        Transformation matrix (for scaling/rotation) passed to
        `Plotter.camera.model_transform_matrix`.
    notebook : bool
        Set to `True` for rendering in a notebook.
    """
    grid = pv.read(mesh_file)
    p = pv.Plotter(notebook=notebook)
    p.set_background(color="k")
    p.add_mesh(grid.copy(), show_edges=True, color="w")
    p.add_axes()
    
    if mtm is not None:
        p.camera.model_transform_matrix = mtm
        
    p.show(cpos=cpos)

    
def get_gmsh2_patches_names(mesh_file):
    """ Get patches names from GMSH v2 file (.msh) for OpenFOAM.
    
    File header is expected to have a structure similar to::

        ```
        $MeshFormat
        2.2 0 8
        $EndMeshFormat
        $PhysicalNames
        6
        2 2 "front"
        2 3 "back"
        2 4 "wall"
        2 5 "inlet"
        2 6 "outlet"
        3 1 "inner"
        $EndPhysicalNames
        ```
        
    Parameters
    ----------
    mesh_file : path-like
        Path to mesh file to be parsed for retrieving data.

    Returns
    -------
    list[str]
        List of patches names as provided in file header.
        
    Raises
    ------
    Exception
        Something is malformed/unexpected in header so that the
        number of patches does not match the expected length.
    ValueError
        Version of GMSH file is not compatible with OpenFOAM.
    """
    names = []
    start = False
    fspec = None
        
    with open(mesh_file) as fp:
        for line in fp.readlines():
            if line.startswith("$MeshFormat"):
                continue

            if line.startswith("$EndMeshFormat"):
                continue

            if line.startswith("$PhysicalNames"):
                start = True
                continue

            if line.startswith("$EndPhysicalNames"):
                break

            if start:
                names.append(line.split()[-1].replace('"', ""))
            else:
                fspec = line[:-1]

        if (gotlen := len(names) - 1) != (expected := int(names[0])):
            raise Exception(f"Bad number of patches: {gotlen} != {expected}")

        if not fspec.startswith("2"):
            raise ValueError(f"OpenFOAM expects GMSH 2 format, got {fspec}")
            
        # TODO check if volumes are always last, so that they can be popped
        # automatically. Also test with a multi-region mesh.
        return names[1:]
